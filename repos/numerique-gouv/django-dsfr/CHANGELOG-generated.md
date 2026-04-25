## Changelog : django-dsfr (30 derniers jours, au 22 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des extensions Markdown, corrigeant un crash potentiel au lancement et permettant une utilisation plus flexible de l'application. De plus, le système de design DSFR a été mis à jour vers la version 1.14.4, apportant les dernières améliorations et corrections de bugs du design système de l'État. Enfin, plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Évolutions fonctionnelles
- Correction d'un crash au lancement de l'application lorsque l'extension Markdown n'est pas activée. [#295](https://github.com/numerique-gouv/django-dsfr/issues/295)
- Ajout de la prise en charge des liens désactivés dans les composants. [#287](https://github.com/numerique-gouv/django-dsfr/issues/287)
- Correction d'un problème lié aux exigences de l'application `dsfr.extras.markdown`. [#304](https://github.com/numerique-gouv/django-dsfr/issues/304)

### Évolutions techniques
- Mise à jour du système de design DSFR vers la version 1.14.4. [#301](https://github.com/numerique-gouv/django-dsfr/issues/301)
- Préparation des releases 3.4.0, 3.4.1 et 3.4.2. [#292](https://github.com/numerique-gouv/django-dsfr/issues/292), [#296](https://github.com/numerique-gouv/django-dsfr/issues/296), [#305](https://github.com/numerique-gouv/django-dsfr/issues/305)

### Autres changements
- Mise à jour de plusieurs dépendances :
    - `lxml` de 6.0.2 à 6.1.0 [#306](https://github.com/numerique-gouv/django-dsfr/issues/306)
    - `pytest` de 9.0.2 à 9.0.3 [#303](https://github.com/numerique-gouv/django-dsfr/issues/303)
    - `cryptography` de 46.0.6 à 46.0.7 [#298](https://github.com/numerique-gouv/django-dsfr/issues/298) et de 46.0.5 à 46.0.6 [#291](https://github.com/numerique-gouv/django-dsfr/issues/291)
    - `django` de 5.2.12 à 5.2.13 [#297](https://github.com/numerique-gouv/django-dsfr/issues/297)
    - `pygments` de 2.19.2 à 2.20.0
    - `black` de 26.1.0 à 26.3.1
    - `requests` de 2.32.5 à 2.33.0 [#290](https://github.com/numerique-gouv/django-dsfr/issues/290)
