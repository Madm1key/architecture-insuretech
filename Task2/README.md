# Task 2 — Horizontal Pod Autoscaler

Нагрузочное тестирование приложения `scaletestapp` в
minikube с автомасштабированием по памяти (HPA).

## Требования

- [minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [uvx](https://docs.astral.sh/uv/)

## Запуск кластера

```bash
minikube start
```

Включить metrics-server (нужен для HPA):

```bash
minikube addons enable metrics-server
```

## Деплой приложения

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

Дождаться готовности подов:

```bash
kubectl wait --for=condition=ready pod -l app=scaletestapp --timeout=120s
```

## Проброс порта

```bash
kubectl port-forward service/scaletestapp 8080:8080
```

## Запуск нагрузочного тестирования

В отдельном терминале (пока активен `port-forward`):

```bash
uvx locust -f locustfile.py --host http://localhost:8080
```

Открыть веб-интерфейс: [http://localhost:8089](http://localhost:8089)

## Наблюдение за автомасштабированием

```bash
# Статус HPA
kubectl get hpa

# Количество подов
kubectl get pods
```

## Остановка и полное удаление кластера

Полностью удалить кластер minikube:

```bash
minikube delete --all --purge
```

Флаг `--purge` удаляет все профили и локальные данные minikube.
