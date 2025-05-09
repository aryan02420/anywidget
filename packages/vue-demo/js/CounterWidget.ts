import { createRender } from "@anywidget/vue";
import CounterWidget from "./CounterWidget.vue";

const render = createRender(CounterWidget);

export default { render };