import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export const sendMessage = async (query) => {

    try {

        const response = await api.post("/chat", {
            query,
        });

        console.log("SUCCESS");
        console.log(response.data);

        return response.data;

    } catch (error) {

        console.log("AXIOS ERROR");
        console.log(error);

        if (error.response) {
            console.log("Status:", error.response.status);
            console.log("Data:", error.response.data);
        }

        throw error;
    }

};