const API_BASE = "http://localhost:8000";

const ENDPOINTS = {
    comentarios: {
        create: "/comentarios",
        read_all: "/comentarios",
        read_one: (id) => `/comentarios/${id}`,
        update: (id) => `/comentarios/${id}`,
        delete: (id) => `/comentarios/${id}`
    },
    productos: {
        create: "/productos",
        read_all: "/productos",
        read_one: (id) => `/productos/${id}`,
        update: (id) => `/productos/${id}`,
        delete: (id) => `/productos/${id}`
    },
    barberos: {
        create: "/barberos",
        read_all: "/barberos",
        read_one: (id) => `/barberos/${id}`,
        update: (id) => `/barberos/${id}`,
        delete: (id) => `/barberos/${id}`
    },
    barberias: {
        create: "/barberias",
        read_all: "/barberias",
        read_one: (id) => `/barberias/${id}`,
        update: (id) => `/barberias/${id}`,
        delete: (id) => `/barberias/${id}`
    }
};

