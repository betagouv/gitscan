## Changelog : django-dsfr (30 derniers jours, au 9 avril 2026)

### Résumé
Cette version apporte des corrections importantes pour améliorer la stabilité et l'expérience utilisateur. Une correction a été apportée pour éviter un crash au lancement lorsque l'extension Markdown n'est pas souhaitée. De plus, la prise en charge des liens désactivés a été ajoutée, offrant plus de flexibilité dans la conception des pages. Enfin, des mises à jour de dépendances ont été intégrées pour assurer la sécurité et la compatibilité du projet.

### Évolutions fonctionnelles
- Correction d'un crash au lancement si l'extension Markdown n'est pas activée. [#295](https://github.com/numerique-gouv/django-dsfr/issues/295)
- Ajout de la prise en charge des liens désactivés, permettant de créer des liens visuellement distincts qui ne redirigent pas l'utilisateur. [#287](https://github.com/numerique-gouv/django-dsfr/issues/287)

### Évolutions techniques
- Préparation de la release 3.4.0, incluant des améliorations internes et des corrections. [#292](https://github.com/numerique-gouv/django-dsfr/issues/292)
- Préparation de la release 3.4.1, incluant des corrections et améliorations mineures. [#296](https://github.com/numerique-gouv/django-dsfr/issues/296)

### Autres changements
- Mise à jour de la dépendance `cryptography` de 46.0.5 à 46.0.6 et ensuite à 46.0.7 [#291](https://github.com/numerique-gouv/django-dsfr/issues/291) et [#298](https://github.com/numerique-gouv/django-dsfr/issues/298)
- Mise à jour de la dépendance `django` de 5.2.11 à 5.2.12 puis à 5.2.13 [#286](https://github.com/numerique-gouv/django-dsfr/issues/286) et [#297](https://github.com/numerique-gouv/django-dsfr/issues/297)
- Mise à jour de la dépendance `pygments` de 2.19.2 à 2.20.0
- Mise à jour de la dépendance `black` de 26.1.0 à 26.3.1
- Mise à jour de la dépendance `requests` de 2.32.5 à 2.33.0 [#290](https://github.com/numerique-gouv/django-dsfr/issues/290)
