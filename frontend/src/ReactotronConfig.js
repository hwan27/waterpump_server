import Reactotron from "reactotron-react-js";
import { reactotronRedux } from "reactotron-redux";

Reactotron.configure({ name: "waterpump" })
  .use(reactotronRedux())
  .connect();

export default Reactotron;
