## Changelog : archeologia-pipeline (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, le pipeline a subi une refonte majeure de son interface utilisateur, passant à une nouvelle version du "wizard" (assistant de configuration). Cette refonte vise à améliorer l'expérience utilisateur en guidant l'utilisateur à travers les différentes étapes du traitement des données LiDAR, de la source aux détections d'éléments archéologiques. Des améliorations significatives ont également été apportées à la gestion des modèles de détection et à la gestion des annulations de traitements.

### Évolutions fonctionnelles
- **Nouvelle interface utilisateur (wizard V2):** Refonte complète de l'interface utilisateur pour une expérience plus intuitive et guidée. L'interface est divisée en quatre étapes : source, indices, détection par entités et lancement. [#d9c3f3d](https://github.com/betagouv/archeologia-pipeline/commit/d9c3f3d)
- **Gestion des seuils de confiance:** Possibilité de définir un seuil de confiance par entité pour filtrer les détections et améliorer la symbologie.
- **Nommage des indices paramétré:**  Possibilité de personnaliser le nommage des indices calculés.
- **Annulation des traitements:** Amélioration de la gestion de l'annulation des traitements, avec une annulation propre et fine à chaque étape du pipeline.
- **Informations sur les modèles IA:** Ajout d'une icône d'information (ⓘ) pour afficher des détails sur les modèles d'intelligence artificielle programmés. [#7a6037b](https://github.com/betagouv/archeologia-pipeline/commit/7a6037b)
- **Validation du workflow:** Ajout d'une validation bloquante à l'étape de lancement pour s'assurer que tous les paramètres sont correctement configurés.
- **Barre de progression améliorée:** La barre de progression a été rendue plus lisible avec une épaisseur accrue et un affichage centré du pourcentage.
- **Gestion des fichiers ASC:** Acceptation des fichiers ASC en mode "existing_mnt". [#e398e0e](https://github.com/betagouv/archeologia-pipeline/commit/e398e0e)

### Évolutions techniques
- **Refonte de l'orchestrateur de modèles:**  Nouvel orchestrateur de modèles par entités avec un catalogue et une configuration V2. [#d84fedd](https://github.com/betagouv/archeologia-pipeline/commit/d84fedd)
- **Refactoring de l'annulation:**  Refactorisation du code pour une gestion plus propre et plus efficace de l'annulation des traitements.
- **Régénération de l'index VRT:** L'index VRT est maintenant régénéré systématiquement pour garantir sa cohérence. [#cc0cc82](https://github.com/betagouv/archeologia-pipeline/commit/cc0cc82)
- **Bascule sur le nouveau wizard:** Le code principal a été mis à jour pour utiliser le nouveau wizard V2 et l'ancienne interface utilisateur a été supprimée. [#e3449f5](https://github.com/betagouv/archeologia-pipeline/commit/e3449f5)

### Autres changements
- **Documentation:** Mise à jour de la documentation README et CLAUDE.md pour refléter les changements apportés. [#74c6c28](https://github.com/betagouv/archeologia-pipeline/commit/74c6c28)
- **Mise à jour des checksums:** Mise à jour des checksums pour les fichiers de configuration et de documentation.
- **Bump de version:** Le pipeline a été mis à jour vers la version 0.3.0 puis 0.5.0. [#11298af](https://github.com/betagouv/archeologia-pipeline/commit/11298af)
