## Changelog : quefairedemesobjets (30 derniers jours, au 04/11/2026)

### Résumé
Ce mois-ci a été marqué par une avancée majeure dans la gestion des données avec l'introduction du Machine Learning pour la déduplication des acteurs. Le projet a également vu le déploiement d'un tout nouveau système de gestion des suggestions pour les administrateurs, basé sur une architecture moderne (Django + React), et la poursuite de la transition vers l'Assistant V2 pour les utilisateurs.

### Évolutions fonctionnelles
- **Nouveau système de gestion des suggestions (Interface Admin) :** Mise en place d'une interface complète permettant la revue, la validation par ligne, les actions de masse, et la gestion de cohortes de suggestions via des onglets et des menus de sélection [#3487, #3488, #3489, #3490, #3491, #3492, #3493, #3533, #3534, #3536].
- **Assistant V2 :** Redirection automatique des utilisateurs existants vers la nouvelle version de l'assistant [#3480] et correction du suivi des slugs de synonymes [#3497].
- **Accessibilité et UX :** Amélioration de l'accessibilité des boutons dans les modales [#3590] et correction de la persistance de la géolocalisation dans les iframes lors de redirections vers d'autres domaines [#3498].
- **Interface Admin :** Ajustement du design CSS pour optimiser l'affichage des menus de sélection [#3496].

### Évolutions techniques
- **Données & Machine Learning :** Implémentation d'une approche par Machine Learning pour la déduplication des acteurs [#3176] et optimisation des pipelines d'enrichissement de données via Airflow et DBT [#3530, #3532, #3562].
- **Architecture :** Mise en place d'un nouveau socle architectural combinant Django et React pour le module de suggestions [#3488] et migration des paramètres des workers vers le module API [#3463].
- **Infrastructure & DevOps :** Résolution de problèmes de gestion de cache dans la CI [#3569], correction de la gestion du cache Nginx pour l'assistant [#3486] et suppression de l'infrastructure Metabase en environnement de préproduction [#3409].
- **Observabilité & Configuration :** Amélioration de la précision des logs (Airflow et erreurs de commandes bash) [#3522, #531] et paramétrage du port de la base de données via variable d'environnement pour le développement local [#3415].
- **Base de données :** Mise à jour des droits de lecture sur l'ensemble du schéma [#3405].

### Autres changements
- **Documentation :** Ajout de la documentation relative au nouveau système de suggestions administratives [#3494].
