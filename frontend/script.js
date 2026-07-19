const API_URL = "http://127.0.0.1:8000/generate";

// ---------------- Elements ----------------

const topic = document.getElementById("topic");
const contentType = document.getElementById("contentType");
const tone = document.getElementById("tone");
const wordCount = document.getElementById("wordCount");

const generateBtn = document.getElementById("generateBtn");
const copyBtn = document.getElementById("copyBtn");
const downloadBtn = document.getElementById("downloadBtn");

const contentOutput = document.getElementById("contentOutput");
const seoOutput = document.getElementById("seoOutput");

const words = document.getElementById("words");
const reading = document.getElementById("reading");
const paragraphs = document.getElementById("paragraphs");
const sentences = document.getElementById("sentences");

const grammarScore = document.getElementById("grammarScore");
const readabilityScore = document.getElementById("readabilityScore");
const seoScore = document.getElementById("seoScore");
const overallScore = document.getElementById("overallScore");

const pipeline = [
    document.getElementById("step1"),
    document.getElementById("step2"),
    document.getElementById("step3"),
    document.getElementById("step4"),
    document.getElementById("step5"),
    document.getElementById("step6")
];

// ---------------- Pipeline ----------------

function resetPipeline() {

    pipeline.forEach(step => {

        step.classList.remove(
            "active",
            "completed",
            "error"
        );

    });

}

async function animatePipeline() {

    resetPipeline();

    for (let i = 0; i < pipeline.length; i++) {

        pipeline[i].classList.add("active");

        await new Promise(resolve =>
            setTimeout(resolve, 350)
        );

        pipeline[i].classList.remove("active");

        pipeline[i].classList.add("completed");

    }

}

// ---------------- Statistics ----------------

function updateStatistics(text) {

    const wordArray = text.trim().split(/\s+/).filter(Boolean);

    const wordCount = wordArray.length;

    words.textContent = wordCount;

    reading.textContent = Math.max(
        1,
        Math.ceil(wordCount / 200)
    );

    paragraphs.textContent =
        text
            .split(/\n+/)
            .filter(p => p.trim() !== "")
            .length;

    sentences.textContent =
        text
            .split(/[.!?]+/)
            .filter(s => s.trim() !== "")
            .length;

}

// ---------------- Scores ----------------

function updateScores(data) {

    grammarScore.textContent =
        data.grammar ?? "-";

    readabilityScore.textContent =
        data.readability ?? "-";

    seoScore.textContent =
        data.seo ?? "-";

    overallScore.textContent =
        data.overall ?? "-";

}

// ---------------- Generate ----------------

generateBtn.addEventListener(
    "click",
    generateContent
);

async function generateContent() {

    const topicValue = topic.value.trim();

    if (!topicValue) {

        alert("Please enter a topic.");

        return;

    }

    generateBtn.disabled = true;

    generateBtn.innerText = "Generating...";

    contentOutput.value = "";

    seoOutput.value = "";

    resetPipeline();

    try {

        const animation = animatePipeline();

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                topic: topicValue,

                content_type: contentType.value,

                tone: tone.value,

                word_count: Number(wordCount.value)

            })

        });

        if (!response.ok) {

            throw new Error(
                "Backend Error"
            );

        }

        const data = await response.json();

        await animation;

        contentOutput.value =
            data.content || "";

        seoOutput.value =
            data.seo || "";

        updateStatistics(
            contentOutput.value
        );

        if (data.evaluation) {

            updateScores(
                data.evaluation
            );

        }

    }

    catch (error) {

        console.error(error);

        resetPipeline();

        pipeline.forEach(step =>
            step.classList.add("error")
        );

        alert(
            "Could not connect to backend."
        );

    }

    finally {

        generateBtn.disabled = false;

        generateBtn.innerText =
            "Generate Content";

    }

}

// ---------------- Copy ----------------

copyBtn.addEventListener(
    "click",
    async () => {

        if (!contentOutput.value) {

            alert("Nothing to copy.");

            return;

        }

        await navigator.clipboard.writeText(
            contentOutput.value
        );

        copyBtn.innerText = "Copied!";

        setTimeout(() => {

            copyBtn.innerText = "Copy";

        }, 1500);

    }
);

// ---------------- Download ----------------

downloadBtn.addEventListener(
    "click",
    () => {

        if (!contentOutput.value) {

            alert("Nothing to download.");

            return;

        }

        const blob = new Blob(

            [contentOutput.value],

            {

                type: "text/plain"

            }

        );

        const url =
            URL.createObjectURL(blob);

        const a =
            document.createElement("a");

        a.href = url;

        a.download = "generated_content.txt";

        document.body.appendChild(a);

        a.click();

        document.body.removeChild(a);

        URL.revokeObjectURL(url);

    }
);

resetPipeline();