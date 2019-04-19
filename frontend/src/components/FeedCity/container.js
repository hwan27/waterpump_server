import React, { Component } from "react";
import FeedCity from "./presenter";

class Container extends Component {
  state = {
    isClicked: false
  };
  render() {
    const { isClicked } = this.state;
    return (
      <FeedCity clicked={isClicked} click={this._clicked} {...this.props} />
    );
  }
  _clicked = () => {
    this.setState({ isClicked: true });
  };
}

// const Container = props => <FeedCity {...props} />;

export default Container;
