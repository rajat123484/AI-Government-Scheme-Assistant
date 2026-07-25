// ============================================================
// SchemeAI - Recommendations
// ============================================================


// ============================================================
// ELEMENTS
// ============================================================

const container =
    document.getElementById(
        "recommendationsContainer"
    );

const profileSummary =
    document.getElementById(
        "profileSummary"
    );

const resultCount =
    document.getElementById(
        "resultCount"
    );

const emptyState =
    document.getElementById(
        "emptyState"
    );


// ============================================================
// LOAD DATA
// ============================================================

const storedData =
    sessionStorage.getItem(
        "schemeRecommendations"
    );


const storedProfile =
    sessionStorage.getItem(
        "userProfile"
    );


// ============================================================
// CHECK DATA
// ============================================================

if (!storedData) {

    showEmptyState();

} else {

    try {

        const data =
            JSON.parse(storedData);

        const profile =
            storedProfile
                ? JSON.parse(storedProfile)
                : null;


        if (profile) {

            renderProfile(
                profile
            );

        }


        renderRecommendations(
            data
        );

    }

    catch (error) {

        console.error(
            "Error loading recommendations:",
            error
        );

        showEmptyState();

    }

}


// ============================================================
// PROFILE SUMMARY
// ============================================================

function renderProfile(profile) {


    profileSummary.innerHTML = `

        <div class="summary-title">

            <span class="summary-icon">
                👤
            </span>

            <div>

                <h3>
                    Your Profile
                </h3>

                <p>
                    Recommendations generated using your details
                </p>

            </div>

        </div>


        <div class="profile-tags">

            <span>
                Age: ${profile.age}
            </span>

            <span>
                ${escapeHTML(profile.gender)}
            </span>

            <span>
                ${escapeHTML(profile.occupation)}
            </span>

            <span>
                ${escapeHTML(profile.state)}
            </span>

            <span>
                Income: ₹${Number(profile.income).toLocaleString("en-IN")}
            </span>

            <span>
                ${escapeHTML(profile.category)}
            </span>

        </div>

    `;

}


// ============================================================
// RENDER RECOMMENDATIONS
// ============================================================

function renderRecommendations(data) {


    container.innerHTML = "";


    let responseText = "";


    // --------------------------------------------------------
    // GET BACKEND RESPONSE
    // --------------------------------------------------------

    if (
        data &&
        data.data &&
        data.data.response
    ) {

        responseText =
            data.data.response;

    }


    if (!responseText) {

        showEmptyState();

        return;

    }


    // --------------------------------------------------------
    // REMOVE HEADER
    // --------------------------------------------------------

    responseText =
        responseText.replace(

            /={5,}[\s\S]*?Recommendation\s*/i,

            ""

        );


    // --------------------------------------------------------
    // SPLIT SCHEMES
    // --------------------------------------------------------

    const schemes =
        responseText
            .split(
                /-{20,}/
            )
            .map(
                item => item.trim()
            )
            .filter(
                item =>
                    item.includes("🏆")
            );


    if (!schemes.length) {

        showEmptyState();

        return;

    }


    resultCount.textContent =

        `${schemes.length} personalized scheme recommendation` +

        (schemes.length > 1
            ? "s"
            : "") +

        " found for your profile";


    // --------------------------------------------------------
    // CREATE CARDS
    // --------------------------------------------------------

    schemes.forEach(

        (scheme, index) => {

            const card =
                createSchemeCard(
                    scheme,
                    index
                );

            container.appendChild(
                card
            );

        }

    );

}


// ============================================================
// CREATE SCHEME CARD
// ============================================================

function createSchemeCard(
    text,
    index
) {


    const schemeName =
        extractSection(
            text,
            "🏆",
            "⭐"
        );


    const matchScore =
        extractSection(
            text,
            "⭐ Match Score",
            "✅"
        );


    const whyMatch =
        extractSection(
            text,
            "✅ Why this scheme matches",
            "🎁"
        );


    const benefits =
        extractSection(
            text,
            "🎁 Benefits",
            "📋"
        );


    const eligibility =
        extractSection(
            text,
            "📋 Eligibility",
            "📄"
        );


    const documents =
        extractSection(
            text,
            "📄 Required Documents",
            "🌐"
        );


    const website =
        extractSection(
            text,
            "🌐 Official Website",
            "⚠"
        );


    const notes =
        extractSection(
            text,
            "⚠ Important Notes",
            ""
        );


    const card =
        document.createElement(
            "article"
        );


    card.className =
        "scheme-card";


    card.style.animationDelay =
        `${index * 120}ms`;


    const score =
        matchScore.trim();


    let scoreClass =
        "medium";


    if (
        score.toLowerCase()
            .includes("high")
    ) {

        scoreClass =
            "high";

    }

    else if (
        score.toLowerCase()
            .includes("low")
    ) {

        scoreClass =
            "low";

    }


    const cleanWebsite =
        extractURL(
            website
        );


    card.innerHTML = `

        <div class="scheme-card-header">


            <div class="scheme-number">

                ${index + 1}

            </div>


            <h2>

                ${escapeHTML(
                    cleanText(
                        schemeName
                    )
                )}

            </h2>


            <span class="score ${scoreClass}">

                ${escapeHTML(
                    cleanText(score)
                )}

            </span>


        </div>


        <div class="scheme-divider"></div>


        <div class="scheme-content">


            <div class="scheme-section full">

                <h4>
                    WHY THIS SCHEME MATCHES
                </h4>

                <p>
                    ${formatText(
                        whyMatch
                    )}
                </p>

            </div>


            <div class="scheme-columns">


                <div class="scheme-section">

                    <h4>
                        BENEFITS
                    </h4>

                    <p>
                        ${formatText(
                            benefits
                        )}
                    </p>

                </div>


                <div class="scheme-section">

                    <h4>
                        ELIGIBILITY
                    </h4>

                    <p>
                        ${formatText(
                            eligibility
                        )}
                    </p>

                </div>


            </div>


            <div class="scheme-section">

                <h4>
                    REQUIRED DOCUMENTS
                </h4>

                <p>
                    ${formatText(
                        documents
                    )}
                </p>

            </div>


            ${
                cleanWebsite
                    ? `

                    <div class="website-section">

                        <h4>
                            OFFICIAL WEBSITE
                        </h4>

                        <a
                            href="${cleanWebsite}"
                            target="_blank"
                            rel="noopener noreferrer"
                            class="website-btn"
                        >

                            Visit Official Website
                            →

                        </a>

                    </div>

                    `
                    : ""

            }


            ${
                notes.trim()
                    ? `

                    <div class="important-note">

                        <strong>
                            ⚠ Important Note
                        </strong>

                        <p>
                            ${formatText(
                                notes
                            )}
                        </p>

                    </div>

                    `
                    : ""

            }


        </div>

    `;


    return card;

}


// ============================================================
// EXTRACT SECTION
// ============================================================

function extractSection(
    text,
    start,
    end
) {


    const startIndex =
        text.indexOf(
            start
        );


    if (
        startIndex === -1
    ) {

        return "";

    }


    const contentStart =
        startIndex +
        start.length;


    let contentEnd =
        text.length;


    if (end) {

        const foundEnd =
            text.indexOf(
                end,
                contentStart
            );


        if (
            foundEnd !== -1
        ) {

            contentEnd =
                foundEnd;

        }

    }


    return text
        .substring(
            contentStart,
            contentEnd
        )
        .trim();

}


// ============================================================
// EXTRACT URL
// ============================================================

function extractURL(
    text
) {


    const match =
        text.match(
            /https?:\/\/[^\s]+/i
        );


    return match
        ? match[0].replace(
            /[.,)]$/,
            ""
        )
        : "";

}


// ============================================================
// CLEAN TEXT
// ============================================================

function cleanText(
    text
) {


    return text

        .replace(
            /[*#_]/g,
            ""
        )

        .replace(
            /\n+/g,
            " "
        )

        .trim();

}


// ============================================================
// FORMAT TEXT
// ============================================================

function formatText(
    text
) {


    if (!text) {

        return "Information not available.";

    }


    return escapeHTML(
        cleanText(
            text
        )
    );

}


// ============================================================
// ESCAPE HTML
// ============================================================

function escapeHTML(
    text
) {


    const div =
        document.createElement(
            "div"
        );


    div.textContent =
        text;


    return div.innerHTML;

}


// ============================================================
// EMPTY STATE
// ============================================================

function showEmptyState() {


    container.innerHTML =
        "";


    emptyState.classList.remove(
        "hidden"
    );


    resultCount.textContent =
        "No recommendations available.";

}