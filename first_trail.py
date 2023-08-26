import mlflow


def calculate_sum(x,y):
    return x*y

if __name__ == '__main__':
    # starting the mlflow server
    with mlflow.start_run():
        x,y = 15,10
        res = calculate_sum(x,y)
        #Tracking the experiment with the mlflow
        mlflow.log_param('x',x)
        mlflow.log_param('y',y)
        mlflow.log_param('res',res)