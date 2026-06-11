## Changelog : benefriches (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité des tests automatisés, l'amélioration de l'expérience utilisateur dans la création de projets, et l'ajout de nouvelles fonctionnalités pour le calcul des impacts, notamment concernant les statistiques et la comparaison des scénarios. Des optimisations de performance et de sécurité ont également été apportées à l'API.

### Évolutions fonctionnelles
- Amélioration du formulaire de création de projet :
    - Affichage de la surface totale du site sur l'étape des espaces verts publics.
    - Pré-remplissage de la surface des nouveaux bâtiments lors de leur création.
    - Gestion améliorée des étapes de réutilisation/construction des bâtiments.
    - Correction de l'affichage des zones urbaines dans le formulaire.
- Calcul des impacts :
    - Ajout d'un endpoint API pour calculer les impacts d'un site dans un scénario "statu quo".
    - Amélioration du calcul des impacts économiques, incluant la prise en compte de l'évolution du PIB et des coûts liés à l'étalement urbain.
    - Ajout d'informations supplémentaires dans les résultats de l'endpoint de statistiques.
    - Correction d'erreurs dans le calcul des impacts liés à la conservation de la nature et à la consommation d'énergie.
- Visualisation des données :
    - Refonte de l'onglet de comparaison des impacts pour afficher les coûts d'inaction et de l'étalement urbain.
    - Amélioration de l'affichage du graphique du seuil de rentabilité.
- Intégration :
    - Ajout d'un script pour importer des projets de reconversion à partir d'un fichier CSV.
    - Ajout d'un script pour exporter les impacts au format CSV.
- Lien vers la base de données DVF (Valeur Foncière) ajouté dans les informations du formulaire.

### Évolutions techniques
- Infrastructure et CI/CD :
    - Mise à jour de pnpm vers la version 11.5.2.
    - Amélioration de la configuration des ports pour les tests.
    - Ajout de cache pour les builds d'images Docker dans les tests E2E.
    - Ajout d'un throttleur pour la sécurité de l'API.
    - Utilisation de Sonnet pour l'exécution des tests E2E.
- Tests :
    - Correction de problèmes de flakiness dans les tests E2E, notamment en utilisant des mocks pour les APIs externes (PVGIS et CRM).
    - Amélioration de la gestion des timeouts et des logs dans les tests E2E.
    - Mise à jour de Playwright vers la version 1.60.0.
    - Ajout de Talisman pour la détection de secrets dans le code.
- API :
    - Refactorisation du code pour améliorer la structure et la documentation.
    - Amélioration de la gestion des erreurs et du logging.
    - Séparation du code d'import/export des données ADEME.
- Documentation :
    - Spécification de la version attendue de PostgreSQL dans le fichier README.
    - Mise à jour de la documentation CLAUDE.md pour suivre les bonnes pratiques.

### Autres changements
- Correction de petites erreurs et améliorations de la lisibilité du code.
- Suppression de code de débogage temporaire.
- Mise à jour des dépendances (hors mises à jour de routine).
