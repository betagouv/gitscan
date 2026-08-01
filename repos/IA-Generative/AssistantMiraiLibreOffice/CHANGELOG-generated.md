## Changelog : AssistantMiraiLibreOffice (30 derniers jours, au 05 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la fiabilité et l'expérience utilisateur de la mise à jour de l'extension, ainsi que sur l'intégration SSO (Single Sign-On) avec Mirai. Des corrections ont été apportées pour gérer les échecs de téléchargement et améliorer le processus d'installation. Une nouvelle fonctionnalité permet d'ouvrir directement le dossier de l'extension pour faciliter le diagnostic en cas de problème.

### Évolutions fonctionnelles
- Ajout d'un bouton "Ouvrir le dossier" dans la boîte de dialogue de mise à jour bloquée, permettant d'accéder directement au dossier de l'extension pour le débogage et le diagnostic. [#7](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/7)
- Amélioration du message d'erreur affiché en cas d'échec de mise à jour, avec des instructions pour une installation manuelle.
- Correction de l'affichage du bouton "Ouvrir le dossier" qui était invisible dans l'infobox, il est maintenant affiché dans la querybox. [#12](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/12)
- Intégration du SSO Mirai via les variables d'environnement `KEYCLOAK_*`. [#2](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/2)
- Ajout d'un menu contextuel (travaux en cours, corrections et traductions). [#88819ce](https://github.com/IA-Generative/AssistantMiraiLibreOffice/commit/88819ce)

### Évolutions techniques
- Refonte du mécanisme de mise à jour pour une installation "in-process" via `ExtensionManager`, améliorant la fiabilité et la gestion des erreurs. [#19](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/19)
- Implémentation d'un système de repli (failover) pour le téléchargement des mises à jour, garantissant une disponibilité accrue. [#16](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/16)
- Amélioration de la gestion des erreurs lors de la mise à jour, avec une dégradation propre et une prévention des boucles infinies. [#3](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/3)
- Optimisation de la récupération de la configuration via un système de cache-first, de timeout court et de failover. [#3](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/3)
- Correction d'un problème d'envoi des credentials lors de la mise à jour. [#20](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/20)
- Utilisation du singleton `ExtensionManager` pour l'installation in-process. [#14](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/14)
- Amélioration du redémarrage de LibreOffice après la mise à jour, en utilisant un thread principal. [#21](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/21)

### Autres changements
- Mise à jour de la documentation pour refléter le nouveau mécanisme de mise à jour et les liens de suivi. [#11](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/11)
- Mise à jour du fichier README et du guide du développeur. [#2](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/2)
- Plusieurs mises à jour de version (0.0.1.0.15 -> 0.0.1.0.17 -> 0.0.1.0.19 -> 0.0.1.0.22) avec des corrections et des améliorations mineures.
- Ajout de la possibilité de désactiver la vérification TLS par URL via `bootstrap_insecure_urls`. [#2cf61bb](https://github.com/IA-Generative/AssistantMiraiLibreOffice/commit/2cf61bb)
