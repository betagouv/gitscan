## Changelog : territoires-en-transitions (30 derniers jours, au 04 septembre 2026)

### Résumé
Ce mois a été marqué par une avancée majeure sur le parcours PCAET, avec l'automatisation de l'instruction et une gestion plus fine des diagnostics (vulnérabilités, documents, avis). L'authentification a été modernisée grâce à l'intégration du protocole OIDC (ProConnect/MonCompteAdeme), et l'interface utilisateur a bénéficié d'une refonte importante pour améliorer la clarté des parcours de labellisation et de transition écologique.

### Évolutions fonctionnelles
- **Parcours PCAET & Démarches** :
    - Mise en place d'un parcours d'instruction complet : dépôt d'avis, notification des contacts, et gestion des étapes de validation par les services instructeurs (DREAL, Régions, DDT).
    - Amélioration du diagnostic : ajout d'une étape de saisie des vulnérabilités (obligatoire pour clôturer le diagnostic) et navigation pas à pas facilitée.
    - Gestion documentaire enrichie : possibilité de lier plusieurs plans à une démarche, accès sécurisé via des URLs signées et gestion plus intuitive des documents de la démarche.
    - Nouveau tableau de bord pour le suivi des demandes d'avis et statistiques associées.
- **Labellisation & Référentiels** :
    - Déploiement de la bascule "Transition Écologique" (TE) de bout en bout.
    - Ajout de nouveaux onglets dans les référentiels : bibliothèque de documents, journal d'activité et synthèse de l'état des lieux.
    - Extension des droits : les super-administrateurs peuvent désormais remplacer un rapport d'audit.
- **Authentification & Profils** :
    - Intégration de la connexion via OIDC (ProConnect et MonCompteAdeme) avec gestion automatique de la liaison d'identité et des profils utilisateurs.
- **Interface Utilisateur (UI)** :
    - Amélioration de la navigation et de la clarté : mise à jour massive des libellés (wording), ajout de boutons "split" et de variantes de boutons (danger, lien).
    - Optimisation de l'affichage : en-têtes de tableaux fixes (sticky), gestion des bannières d'information mémorisées et amélioration de l'accessibilité clavier.

### Évolutions techniques
- **Architecture & Backend** :
    - Refonte profonde des modules "Référentiels", "Plans" et "Diagnostic" pour une meilleure séparation des responsabilités (utilisation de repositories et de services dédiés).
    - Migration et normalisation des données (passage au camelCase pour de nombreux modèles et types).
    - Optimisation de la gestion des fichiers et des accès aux documents via le backend.
- **Infrastructure & DevOps** :
    - Optimisation de la CI/CD : accélération des tests E2E, exécution des tests par périmètre affecté et amélioration de la configuration Dependabot.
    - Amélioration de l'expérience de développement (DevX) : nouveaux scripts de configuration locale, optimisation de la construction des images Docker et gestion améliorée des variables d'environnement.
- **Observabilité** :
    - Automatisation de la synchronisation quotidienne des groupes utilisateurs avec PostHog via un job cron.

### Autres changements
- **Documentation** : Mise à jour des guides d'utilisation (authentification, règles de wording pour les agents).
- **Qualité du code** : Nettoyage important des composants obsolètes, suppression de code mort et renforcement de la couverture de tests (Vitest et Playwright).
