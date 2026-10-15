## Changelog : federation (30 derniers jours, au 14 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes avec l'introduction de la gestion des demandes XDA (approbation et rejet) et la mise en œuvre de l'authentification multi-appareils. Ces évolutions, accompagnées de renforcements de la sécurité et d'améliorations de l'interface utilisateur, visent à fluidifier l'expérience des professionnels tout en consolidant la robustesse du système.

### Évolutions fonctionnelles
- **Gestion des demandes XDA** : Introduction du cycle de vie des demandes (approbation et rejet) avec un affichage visuel amélioré via des emojis pour faciliter la revue [#1727](https://github.com/proconnect-gouv/federation/issues/1727), [#1725](https://github.com/proconnect-gouv/federation/issues/1725).
- **Authentification** : Mise en œuvre de l'authentification multi-appareils (cross-device) pour une meilleure flexibilité [#1717](https://github.com/proconnect-gouv/federation/issues/1717).
- **Expérience utilisateur (UX)** : 
    - Amélioration de la lisibilité avec un nouveau formatage de l'User-Agent [#1724](https://github.com/proconnect-gouv/federation/issues/1724).
    - Affichage conditionnel de l'URL de déconnexion [#1684](https://github.com/proconnect-gouv/federation/issues/1684).
    - Pré-sélection automatique de l'Identifiant Financier (FI) en cas de présence de plusieurs FI [#1593](https://github.com/proconnect-gouv/federation/issues/1593).
- **Corrections** : Résolution de problèmes d'affichage en production [#1661](https://github.com/proconnect-gouv/federation/issues/1661) et gestion des erreurs d'accès RIE [#1690](https://github.com/proconnect-gouv/federation/issues/1690).

### Évolutions techniques
- **Sécurité** : 
    - Restriction de l'accès par défaut aux revendications de rôles (roles claim) [#1687](https://github.com/proconnect-gouv/federation/issues/1687).
    - Retrait de l'URL PAR des métadonnées de découverte pour renforcer la confidentialité [#1647](https://github.com/proconnect-gouv/federation/issues/1647).
- **Infrastructure & CI/CD** : 
    - Migration de l'environnement de développement de Yarn 1.x vers npm [#1624](https://github.com/proconnect-gouv/federation/issues/1624).
    - Fixation de la version de Docker Compose (v5.5.1) [#9393f3f](https://github.com/proconnect-gouv/federation/issues/9393f3f).
    - Optimisation du workflow de build Docker avec l'ajout de permissions spécifiques [#1625](https://github.com/proconnect-gouv/federation/issues/1625).
    - Correction de la gestion des assets (JS/CSS) pour le service d'administration en production [#0d6276a](https://github.com/proconnect-gouv/federation/issues/0d6276a).
- **Refactoring & Optimisation** : 
    - Modernisation des imports en remplaçant les chemins `@fc/*` par des imports natifs package.json [#1716](https://github.com/proconnect-gouv/federation/issues/1716).
    - Suppression de l'outil obsolète `typeorm-fixtures-cli` [#59ddc29](https://github.com/proconnect-gouv/federation/issues/59ddc29) et nettoyage de champs inutilisés (`statusUrl`) [#c672a68](https://github.com/proconnect-gouv/federation/issues/c672a68).
- **Observabilité & Qualité** : 
    - Ajout du monitoring de santé pour le service de messagerie (mailer) [#8061589](https://github.com/proconnect-gouv/federation/issues/8061589).
    - Amélioration de la journalisation des alertes Hyperbridge [#1703](https://github.com/proconnect-gouv/federation/issues/1703).
    - Ajout d'un banc d'essai E2E pour le TestingBench [#1627](https://github.com/proconnect-gouv/federation/issues/1627).

### Autres changements
- **SEO & Administration** : Ajout d'un fichier `robots.txt` pour empêcher l'indexation des pages d'administration par les moteurs de recherche [#1628](https://github.com/proconnect-gouv/federation/issues/1628).
- **Mise à jour de package** : Actualisation du package ProConnect Identité pour assurer la compatibilité avec l'Annuaire des Entreprises.
