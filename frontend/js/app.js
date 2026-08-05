// ============================================================
// SchemeAI - Profile Form
// ============================================================


// IMPORTANT:
// Change this if your FastAPI backend runs on another port.

const API_BASE_URL = "https://ai-government-scheme-assistant-production.up.railway.app";


// ============================================================
// ELEMENTS
// ============================================================

const profileForm = document.getElementById("profileForm");

const submitBtn = document.getElementById("submitBtn");

const btnText = document.getElementById("btnText");

const loadingOverlay = document.getElementById("loadingOverlay");


// ============================================================
// FORM SUBMIT
// ============================================================

profileForm.addEventListener("submit", async function (event) {

    event.preventDefault();


    // --------------------------------------------------------
    // GET FORM VALUES
    // --------------------------------------------------------

    const profile = {

        age: Number(
            document.getElementById("age").value
        ),

        gender:
            document.getElementById("gender").value,

        occupation:
            document.getElementById("occupation").value,

        state:
            document.getElementById("state").value,

        income: Number(
            document.getElementById("income").value
        ),

        category:
            document.getElementById("category").value,

        disability:
            document.getElementById("disability").value

    };


    // --------------------------------------------------------
    // VALIDATION
    // --------------------------------------------------------

    if (
        !profile.age ||
        !profile.gender ||
        !profile.occupation ||
        !profile.state ||
        !profile.income ||
        !profile.category ||
        !profile.disability
    ) {

        alert(
            "Please complete all required fields."
        );

        return;

    }


    // --------------------------------------------------------
    // LOADING STATE
    // --------------------------------------------------------

    submitBtn.disabled = true;

    btnText.textContent =
        "Finding Schemes...";

    loadingOverlay.classList.remove(
        "hidden"
    );


    try {


        // ----------------------------------------------------
        // CALL RECOMMENDATION API
        // ----------------------------------------------------

        const response = await fetch(

            `${API_BASE_URL}/recommendation/`,

            {

                method: "POST",

                headers: {

                    "Content-Type":
                        "application/json"

                },

                body:
                    JSON.stringify(profile)

            }

        );


        // ----------------------------------------------------
        // CHECK RESPONSE
        // ----------------------------------------------------

        if (!response.ok) {

            throw new Error(
                `Server Error: ${response.status}`
            );

        }


        const result =
            await response.json();


        // ----------------------------------------------------
        // SAVE DATA
        // ----------------------------------------------------

        sessionStorage.setItem(

            "schemeRecommendations",

            JSON.stringify(result)

        );


        sessionStorage.setItem(

            "userProfile",

            JSON.stringify(profile)

        );


        // ----------------------------------------------------
        // REDIRECT
        // ----------------------------------------------------

        window.location.href =
            "recommendations.html";


    }


    catch (error) {


        console.error(
            "Recommendation Error:",
            error
        );


        alert(

            "Unable to connect to the backend.\n\n" +

            "Please make sure your FastAPI server is running."

        );


    }


    finally {


        submitBtn.disabled =
            false;

        btnText.textContent =
            "Find My Schemes";

        loadingOverlay.classList.add(
            "hidden"
        );

    }

});