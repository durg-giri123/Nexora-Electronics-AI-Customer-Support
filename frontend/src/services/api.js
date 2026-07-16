import axios from "axios";

const api = axios.create({
  baseURL: "https://nexora-backend-syl2.onrender.com",
});

export async function sendMessage(query) {
  const response = await api.post("/chat", {
    query,
  });

  return response.data;
}

export default api;