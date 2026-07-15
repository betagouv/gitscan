## Changelog : agreste (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la recherche, avec l'ajout de filtres et la correction de problèmes de doublons. Des efforts ont également été déployés pour améliorer la gestion des médias, l'automatisation des déploiements et la robustesse de l'application, notamment via des scripts de diagnostic et des corrections de bugs. Enfin, des améliorations ont été apportées à l'interface utilisateur et à la gestion des traductions.

### Évolutions fonctionnelles
- **Recherche :** Ajout de filtres de recherche avancés (facettes) permettant un affinement plus précis des résultats. Les thèmes sont désormais affichés au-dessus des collections dans les filtres. [#32](https://github.com/betagouv/agreste/pull/32), [#33](https://github.com/betagouv/agreste/pull/33)
- **Publications :** Amélioration du bloc "Publications récentes" avec des options de personnalisation (libellé du bouton, filtrage des résultats). [#21](https://github.com/betagouv/agreste/pull/21)
- **Interface utilisateur :**
    - Ajout de la possibilité de choisir le type de balise (heading) dans le stepper.
    - Amélioration de l'affichage des tags sélectionnés.
    - Correction d'un bug d'alignement de div dans l'éditeur de texte riche.
- **Médias :** Scripts améliorés pour la sauvegarde et la restauration des médias.

### Évolutions techniques
- **CI/CD :**
    - Mise en place d'un workflow GitHub Actions pour la création et la publication des releases sur PyPi. [#18](https://github.com/betagouv/agreste/pull/18)
    - Amélioration du workflow de déploiement sur Scalingo.
    - Correction de bugs dans le workflow de publication.
- **Monitoring :** Ajout de scripts pour surveiller l'utilisation de la mémoire et la latence de Gunicorn. [#31](https://github.com/betagouv/agreste/pull/31)
- **Refactoring :**
    - Refactorisation du code pour maximiser la réutilisation et simplifier la maintenance.
    - Suppression de code redondant dans le module "publications".
- **Tests :** Ajout et amélioration des tests unitaires et d'intégration, notamment pour les templates et les blocs de contenu.
- **Internationalisation (i18n) :** Indépendance des traductions par rapport à `sites_conformes`, correction des outils de traduction. [#34](https://github.com/betagouv/agreste/pull/34), [#35](https://github.com/betagouv/agreste/pull/35)

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés à ProConnect. [#547](https://github.com/betagouv/agreste/pull/547)
- Amélioration de la recette de mise à niveau pour gérer le projet de démonstration. [#527](https://github.com/betagouv/agreste/pull/527)
- Correction d'une erreur 500 lors du changement de type d'en-tête avec une image d'arrière-plan. [#512](https://github.com/betagouv/agreste/pull/512)
- Correction d'une erreur 500 liée à l'absence d'image.
- Diverses corrections de bugs et améliorations de la qualité du code.
- Bump de version : 2.4.0-4.0.1, 2.4.1-4.0.2, 3.1.1-4.0.1.
