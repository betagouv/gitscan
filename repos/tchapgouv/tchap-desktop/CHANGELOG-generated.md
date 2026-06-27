## Changelog : tchap-desktop (30 derniers jours, au 25 juin 2026)

### Résumé
Cette version apporte des améliorations à l'installation de l'application, notamment pour les utilisateurs installant Tchap dans un contexte utilisateur spécifique. Des corrections ont également été apportées concernant le téléchargement de fichiers et la gestion des services. Enfin, la possibilité de mise à jour automatique de l'application a été ajoutée.

### Évolutions fonctionnelles
- **Installation:** Activation de l'installation de l'application dans le contexte utilisateur, permettant une installation plus flexible et adaptée à certains environnements. [#225](https://github.com/tchapgouv/tchap-desktop/pull/225)
- **Téléchargement:** Restriction des noms de fichiers acceptés lors du téléchargement pour améliorer la sécurité et la gestion des fichiers. [#04db955](https://github.com/tchapgouv/tchap-desktop/commit/04db955)
- **Mise à jour:** Implémentation d'un mécanisme de mise à jour automatique de l'application. [#221](https://github.com/tchapgouv/tchap-desktop/pull/221)
- **Installation (Wix):** Ajout d'un dialogue temporaire demandant à l'utilisateur de désinstaller les versions précédentes avant l'installation. [#224](https://github.com/tchapgouv/tchap-desktop/pull/224)

### Évolutions techniques
- **Refactoring:** Suppression des services de l'appel IPC (Inter-Process Communication) pour simplifier l'architecture. [#303b4c4](https://github.com/tchapgouv/tchap-desktop/commit/303b4c4)
- **Dépendances:** Mise à jour des dépendances Cargo et suppression du plugin d'upload Tauri inutilisé. [#f8c13a4](https://github.com/tchapgouv/tchap-desktop/commit/f8c13a4)
- **Wix:** Modifications de la configuration Wix pour permettre l'installation dans le répertoire AppData et tests de différentes configurations. [#41c9c0b](https://github.com/tchapgouv/tchap-desktop/commit/41c9c0b), [#76979c8](https://github.com/tchapgouv/tchap-desktop/commit/76979c8), [#fc8887e](https://github.com/tchapgouv/tchap-desktop/commit/fc8887e), [#a998b97](https://github.com/tchapgouv/tchap-desktop/commit/a998b97)
- **Build Webapp:** Mise à jour du workflow de build de l'application web à partir de GitHub Actions. [#3c8f368](https://github.com/tchapgouv/tchap-desktop/commit/3c8f368)

### Autres changements
- Mises à jour de version : 4.19.8, 4.19.9 et 4.20.0. [#219](https://github.com/tchapgouv/tchap-desktop/pull/219), [#222](https://github.com/tchapgouv/tchap-desktop/pull/222), [#230](https://github.com/tchapgouv/tchap-desktop/pull/230)
