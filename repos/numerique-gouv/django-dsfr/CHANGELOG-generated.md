## Changelog : django-dsfr (30 derniers jours, au 22 avril 2026)

### Résumé
Cette version apporte des améliorations à la gestion de l'extension Markdown, corrige un crash potentiel au lancement, et met à jour le système de design DSFR vers sa version 1.14.4. Plusieurs corrections et améliorations mineures ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- **Markdown :** Correction d'un crash au lancement lorsque l'extension Markdown n'est pas activée [#295](https://github.com/numerique-gouv/django-dsfr/issues/295).
- **Markdown :** Correction des exigences de l'application `dsfr.extras.markdown` [#304](https://github.com/numerique-gouv/django-dsfr/issues/304).
- **Liens :** Ajout de la prise en charge des liens désactivés [#287](https://github.com/numerique-gouv/django-dsfr/issues/287).

### Évolutions techniques
- **DSFR :** Mise à jour du système de design DSFR vers la version 1.14.4 [#301](https://github.com/numerique-gouv/django-dsfr/issues/301).
- **Dépendances :** Mises à jour de plusieurs dépendances :
    - `cryptography` (de 46.0.6 à 46.0.7) [#298](https://github.com/numerique-gouv/django-dsfr/issues/298)
    - `django` (de 5.2.12 à 5.2.13) [#297](https://github.com/numerique-gouv/django-dsfr/issues/297)
    - `pygments` (de 2.19.2 à 2.20.0)
    - `black` (de 26.1.0 à 26.3.1)
    - `requests` (de 2.32.5 à 2.33.0) [#290](https://github.com/numerique-gouv/django-dsfr/issues/290)
- **Préparation des releases :** Préparation des releases 3.4.0, 3.4.1 et 3.4.2 [#292](https://github.com/numerique-gouv/django-dsfr/issues/292), [#296](https://github.com/numerique-gouv/django-dsfr/issues/296), [#305](https://github.com/numerique-gouv/django-dsfr/issues/305).
