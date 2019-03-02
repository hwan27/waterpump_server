import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";
import FeedSector from "components/FeedSector";

const FeedCity = (props, context) => {
  return (
    <div id="pattern">
      <ul className={styles.list}>
        <li>
          <div className={styles.listText}>{props.title}</div>
          <div className={styles.listText}>{props.sector_set.title}</div>
        </li>
      </ul>
    </div>
  );
};

FeedCity.propTypes = {
  title: PropTypes.string.isRequired,
  sector_set: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string,
      pump_set: PropTypes.arrayOf(PropTypes.shape({ title: PropTypes.string }))
    })
  )
};
export default FeedCity;
