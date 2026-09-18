## Changelog : ocr-api (30 derniers jours, au 16 septembre 2026)

### Résumé
Cette période marque une évolution majeure avec la version 0.20.0. Les utilisateurs bénéficient d'une interface client modernisée (affichage en grille) et de nouveaux outils de développement, notamment un SDK TypeScript. L'accent a été mis sur la robustesse de l'authentification, la sécurité renforcée de l'infrastructure et la correction de bugs critiques sur le traitement des documents multi-pages.

### Évolutions fonctionnelles
- **Interface Client** : 
    - Passage d'un affichage des tâches en tableau à une présentation sous forme de grille de tuiles.
    - Amélioration de l'expérience utilisateur avec une pagination correcte et l'ajout d'un bouton de rafraîchissement manuel des tâches.
    - Ajout de liens directs vers la documentation de l'API et GitHub dans le pied de page.
- **SDK** : Introduction d'un nouveau SDK TypeScript/Node.js synchronisé avec les schémas de l'API.
- **Authentification** : 
    - Support complet des jetons de rafraîchissement (refresh tokens) de bout en bout.
    - Ajout de l'authentification par clé API pour les communications machine-to-machine.
    - Ajout d'un endpoint de jeton (password-grant) pour les clients n'utilisant pas de navigateur.
- **Traitement de documents** : Correction d'un bug majeur qui entraînait la perte des pages suivantes (page 2 et plus) lors de l'extraction de fichiers DOCX, PPTX et autres formats multi-pages.
- **Performance** : Activation de la disponibilité du support GPU pour le traitement.

### Évolutions techniques
- **Sécurité** : 
    - Durcissement des images Docker (utilisation d'UID arbitraires, système de fichiers en lecture seule et mise à jour des paquets de base [#469](https://github.com/IA-Generative/ocr-api/pull/469)).
    - Renforcement des contextes de sécurité pour les composants Helm (Postgres, Redis, RustFS).
- **Infrastructure & Déploiement** : 
    - Intégration des charts Helm directement dans le dépôt.
    - Migration vers pnpm 11 et mise à jour de Node.js vers la version 24 LTS.
    - Remplacement de l'image MinIO par RustFS dans la configuration compose.
- **DevOps & DX** : 
    - Refonte complète de l'outillage de développement et des workflows de l'équipe.
    - Optimisation des builds Docker (évite la copie inutile de `node_modules`).
- **Architecture** : 
    - Réorganisation du SDK Python pour une structure plus propre (`sdk/python`).
    - Ajout d'une couche d'authentification dédiée pour les services backend tiers.

### Autres changements
- **Documentation** : 
    - Ajout de guides de configuration pour Keycloak (flux BFF) et pour la sécurité.
    - Amélioration de la documentation de l'API (descriptions des routes, titres et tags).
- **Nettoyage** : Suppression du sous-module d'infrastructure inutilisé.
