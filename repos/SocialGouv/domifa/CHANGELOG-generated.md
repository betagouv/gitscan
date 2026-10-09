## Changelog : domifa (30 derniers jours, au 08/10/2026)

### Résumé
Ce mois-ci, domifa a connu des évolutions significatives axées sur l'amélioration de l'expérience utilisateur et le renforcement de la sécurité. Les principaux changements incluent une refonte visuelle de l'interface (header, logo, couleurs), l'ajout de la gestion des bénéficiaires familiaux, et la mise en place de nouvelles politiques de sécurité pour la gestion des mots de passe.

### Évolutions fonctionnelles
- **Gestion des bénéficiaires** : Ajout de la fonctionnalité de gestion des ayants droit et bénéficiaires au sein des familles [#4291](https://github.com/SocialGouv/domifa/pull/4291).
- **Sécurité des comptes** : 
    - Mise en place d'un renouvellement obligatoire du mot de passe après une période d'inactivité prolongée.
    - Instauration d'une expiration des mots de passe à 60 mois.
    - Ajout de la possibilité de consulter l'historique des changements de mots de passe.
- **Interface Utilisateur (UI) & Ergonomie** :
    - **Identité visuelle** : Mise à jour du header, de la page de connexion et du logo.
    - **Lisibilité** : Ajustement des couleurs des boutons d'accès, des titres et des pastilles d'indicateurs (notamment pour les délais de décision et de passage).
    - **Affichage des données** : Utilisation du nom complet des usagers dans les titres des dossiers et des notes pour une meilleure identification.
    - **Statistiques** : Corrections de l'affichage CSS et alignement des données de statistiques régionales.
- **Nouveautés** : Ajout de la saisie de la date de domiciliation dans l'interface.

### Évolutions techniques
- **Base de données** : Intégration de nouvelles migrations pour supporter la gestion des bénéficiaires et l'historique des mots de passe.
- **Backend & Sécurité** : 
    - Ajout de "guards" pour sécuriser le processus de renouvellement de mot de passe.
    - Amélioration du suivi des emails via le statut de livraison de Brevo.
- **Maintenance & Performance** :
    - Mise à jour de l'environnement de test vers Jest 30.
    - Nettoyage des dépendances obsolètes (notamment OpenTelemetry) et correction de vulnérabilités.
    - Optimisation de la gestion des logs et des événements Sentry.
    - Migration vers la bibliothèque `date-fns` pour une meilleure gestion des dates.

### Autres changements
- **Documentation** : Mise à jour des composants de présentation (FAQ, pages d'impact et de découverte).
