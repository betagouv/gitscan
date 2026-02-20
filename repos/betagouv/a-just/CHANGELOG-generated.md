## Changelog : a-just (30 derniers jours)

### Résumé
Ce changelog couvre les 30 derniers jours d'évolution du projet a-just. Les modifications incluent des corrections de bugs, des améliorations de l'interface utilisateur (notamment sur le simulateur graphique), des mises à jour de l'extracteur de données, et des améliorations significatives du processus de tests automatisés (E2E) avec Cypress, incluant la gestion des rapports et la configuration de l'environnement CI/CD.

### Évolutions fonctionnelles
- Correction d'un bug affectant l'affichage des ratios dans le simulateur graphique. (#440)
- Correction d'un problème lié à l'affichage des étiquettes.
- Correction d'un bug dans l'upload de fichiers Excel.
- Amélioration de l'extracteur de données, notamment la restauration d'un log manquant pour le endpoint `filterListNew` (#418).
- Correction de l'affichage des entrées projetées dans le simulateur graphique.
- Correction d'un bug lié aux sélecteurs de juridiction.
- Amélioration de l'exportation de données dans les situations d'agents.
- Correction de l'affichage des temps avec deux décimales.
- Correction d'un problème lié à l'affichage des tooltips.

### Évolutions techniques
- Amélioration significative du processus de tests E2E avec Cypress :
    - Correction de la configuration du chemin des rapports Cypress.
    - Ajout de la gestion des fichiers PNG générés par les tests.
    - Optimisation de l'image Docker Cypress pour réduire la consommation de mémoire.
    - Mise à jour de l'image Cypress utilisée.
    - Refactorisation du script de tests non-régression pour simplifier la configuration GitHub Actions.
    - Activation et configuration des tests non-régression.
    - Amélioration de la gestion des logs et des erreurs dans les tests.
- Mise à jour de la version du projet.
- Ajout de `package-lock.json` pour le frontend.
- Correction de scripts d'anonymisation.
- Amélioration de la gestion des logs dans l'API.
- Ajout de SSO à la configuration CORS.
- Correction du chemin d'accès aux fichiers dans les actions GitHub.

### Autres changements
- Nettoyage du code et suppression de fichiers inutiles.
- Mise à jour de la documentation.
- Corrections mineures de style et de formatage.
- Modification du cron job pour les tests nocturnes.
- Ajout de logs de débogage pour faciliter le diagnostic des problèmes.
