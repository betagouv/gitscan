## Changelog : eva-serveur (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'une modernisation importante de son interface utilisateur, notamment via l'alignement sur les composants DSFR, et d'une refonte complète du système de génération de documents PDF pour plus de fiabilité. Les capacités de gestion des données (sociodémographiques, SIRET) ont été enrichies, tandis que l'infrastructure a été mise à jour vers les dernières versions de Rails et Ruby pour garantir la pérennité du service.

### Évolutions fonctionnelles
- **Interface utilisateur & Ergonomie** :
    - Refonte de l'écran de connexion : design plus épuré, centré et entièrement responsive.
    - Modernisation des cartes d'actualités : utilisation des composants DSFR, rendu plus cliquable et ajout d'illustrations.
    - Amélioration de l'expérience d'export PDF : ajout d'une fenêtre modale pour suivre la progression de la génération.
    - Optimisation de l'affichage des tableaux et de la navigation pour éviter les défilements horizontaux indésirables.
- **Gestion des données et fonctionnalités** :
    - Enrichissement des exports : intégration des données sociodémographiques et de santé dans les exports d'évaluations.
    - Amélioration de la validation SIRET : distinction plus précise entre un SIRET fermé et invalide, et gestion plus souple pour les administrateurs en cas d'indisponibilité de l'API SIRENE.
    - Nouveaux droits : les conseillers peuvent désormais modifier les informations des bénéficiaires.
    - Outils d'administration : ajout de boutons pour forcer le recalcul des restitutions et affichage du nombre d'événements dans les informations générales.
- **Accessibilité** :
    - Améliorations pour les lecteurs d'écran (champs email, erreurs de connexion) et optimisation des contrastes.

### Évolutions techniques
- **Refonte du moteur PDF** :
    - Migration de la génération de PDF vers des tâches de fond (Sidekiq) avec notifications en temps réel (ActionCable) pour éviter les blocages de l'interface.
    - Amélioration de la robustesse du navigateur Chromium utilisé pour la génération (gestion des crashs, redémarrage automatique, limitation de la consommation mémoire).
- **Mises à jour majeures** :
    - Migration de l'application vers Rails 8.0.5 et Ruby 4.0.6.
- **Performance et Scalabilité** :
    - Optimisation du redimensionnement des images via une répartition des tâches par question.
    - Optimisation des requêtes SQL pour le calcul de complétude et le composant de standardisation.
    - Mise en place de protections contre les rafales de requêtes (rate limiting) via Rack::Attack.
- **Architecture** :
    - Séparation logique des processus et des calculs entre les flux EVA et EVAPRO.

### Autres changements
- **Sécurité** : Blocage des scans de vulnérabilités automatisés (WordPress/OWA) pour réduire le bruit dans les logs.
- **Assets** : Mise à jour des icônes, des favicons et vectorisation de certains éléments graphiques.
- **Tests** : Amélioration de la qualité des données de test et correction de tests instables.
