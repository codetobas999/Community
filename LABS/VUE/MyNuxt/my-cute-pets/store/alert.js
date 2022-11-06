import Vue from 'vue'

const ADD_ALERT = 'ADD_ALERT';
const REMOVE_ALERT = 'REMOVE_ALERT';
const CLEAR_ALERT = 'CLEAR_ALERT';

export const state = () => ({
    alerts: []
})

export const getters = {
    getAll(state) {
        return state.alerts
    }
}

export const mutations = {
    [ADD_ALERT](state, alert) {
        state.alerts.push(alert);
    },
    [REMOVE_ALERT](state, alert) {
        var i = state.alerts.findIndex(it => it.id == alert.id);
        console.log("index: " + i)
        if (i == -1) {
            return;
        }

        clearTimeout(state.alerts[i].timeOut);
        state.alerts.splice(i, 1);
    },
    [CLEAR_ALERT](state) {
        state.alerts = [];
    }
}

export const actions = {
    add({ commit }, { type, message }) {
        let id = Date.now()
        var timeOut = setTimeout(function () {
            commit(REMOVE_ALERT, { id });
        }, 3000);
        commit(ADD_ALERT, {
            id,
            type,
            message,
            show: true,
            timeOut
        });
    },
    remove({ commit }, alert) {
        commit(REMOVE_ALERT, alert);
    },
    clear({ commit }) {
        commit(CLEAR_ALERT);
    }
}