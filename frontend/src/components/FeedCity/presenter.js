import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";

const FeedCity = (props, context) => {
  console.log(props);
  return <div className={styles.feedcity}>{props.title}</div>;
};

FeedCity.propTypes = {
  cities: PropTypes.shape({
    title: PropTypes.string
  })
};
export default FeedCity;
