import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";
import Sector from "components/Sector";

const FeedCity = (props, context) => {
  return (
    <div id="pattern">
      <ul className={styles.list}>
        <li>
          <div className={styles.listText}>
            <span onClick={() => _clicked(props)}>{props.title} </span>
          </div>

          <Sector sectors={props.sector_set} />
        </li>
      </ul>
    </div>
  );
};

const _clicked = props => {
  Sector.props = props;
  console.log(Sector.props.sector_set);
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
