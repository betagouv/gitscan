## Changelog : mcr (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application MCR, notamment en termes d'import de fichiers, de gestion des transcriptions, de robustesse et d'architecture. L'accent a été mis sur la simplification du code, l'amélioration de l'observabilité et l'intégration de nouvelles fonctionnalités pour faciliter l'utilisation quotidienne.

### Évolutions fonctionnelles
- **Import de fichiers :**
    - Ajout d'une fonctionnalité d'import "one-click" pour une expérience utilisateur simplifiée [#908](https://github.com/IA-Generative/mcr/pull/908).
    - Validation du format et de la durée des fichiers avant l'import pour éviter les erreurs [#911](https://github.com/IA-Generative/mcr/pull/911).
    - Détection des échecs d'import bloqués par un proxy et signalement du type d'échec à Sentry [#899](https://github.com/IA-Generative/mcr/pull/899).
- **Transcription :**
    - La diarisation est désormais asynchrone, améliorant la réactivité de l'application [#898](https://github.com/IA-Generative/mcr/pull/898).
    - Création automatique d'un "deliverable" (livrable) de type TRANSCRIPTION à la fin de chaque transcription, avec un lien vers Google Drive [#810](https://github.com/IA-Generative/mcr/pull/810).
    - Gestion améliorée des tâches de transcription pour les réunions supprimées [#806](https://github.com/IA-Generative/mcr/pull/806).
- **Téléchargement :**
    - Ajout d'un script pour télécharger les fichiers d'une réunion depuis S3 [#903](https://github.com/IA-Generative/mcr/pull/903).
- **Interface utilisateur :**
    - Amélioration de l'accessibilité du modal de feedback [#831](https://github.com/IA-Generative/mcr/pull/831).

### Évolutions techniques
- **Architecture :**
    - Refactorisation majeure de l'architecture vers une approche basée sur des "use cases" pour la gestion de la capture, de l'évaluation et du bot [#803](https://github.com/IA-Generative/mcr/pull/803), [#820](https://github.com/IA-Generative/mcr/pull/820), [#822](https://github.com/IA-Generative/mcr/pull/822), [#824](https://github.com/IA-Generative/mcr/pull/824), [#825](https://github.com/IA-Generative/mcr/pull/825), [#828](https://github.com/IA-Generative/mcr/pull/828).
    - Suppression de la machine d'état (state machine) pour la gestion des réunions, simplifiant le code et améliorant la maintenabilité [#861](https://github.com/IA-Generative/mcr/pull/861).
    - Refactorisation de l'infrastructure pour une meilleure organisation et une plus grande cohérence.
- **CI/CD :**
    - Nettoyage et amélioration des workflows CI/CD [#849](https://github.com/IA-Generative/mcr/pull/849).
- **Observabilité :**
    - Intégration de Sentry pour une meilleure surveillance et un signalement des erreurs [#793](https://github.com/IA-Generative/mcr/pull/793).
    - Amélioration de la gestion des erreurs et ajout de logs plus détaillés.
- **Développement local :**
    - Amélioration de la configuration pour le développement local avec Docker, incluant la gestion des réseaux et des images [#811](https://github.com/IA-Generative/mcr/pull/811).
    - Ajout d'une cible "make install" pour faciliter la mise en place de l'environnement de développement [#834](https://github.com/IA-Generative/mcr/pull/834).

### Autres changements
- Documentation mise à jour pour la configuration de Sentry avec 1Password [#909](https://github.com/IA-Generative/mcr/pull/909).
- Documentation mise à jour pour la génération de comptes rendus [#860](https://github.com/IA-Generative/mcr/pull/860).
- Ajout de pre-commit hooks pour la qualité du code et la sécurité [#834](https://github.com/IA-Generative/mcr/pull/834).
- Corrections de fautes de frappe et améliorations de la lisibilité du code.
- Mise à jour des dépendances et corrections de bugs mineurs.
