## Changelog : OpenGateLLM (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de santé des modèles, de gestion des utilisateurs, de prise en charge des formats audio et de sécurité. Des corrections de bugs et des refactorisations ont également été apportées pour améliorer la stabilité et la maintenabilité du projet. La documentation et le processus de déploiement ont également été mis à jour.

### Évolutions fonctionnelles
- Ajout d'une vérification de l'état de santé des modèles pour assurer leur disponibilité et leur bon fonctionnement. [#870](https://github.com/etalab-ia/OpenGateLLM/issues/870)
- Prise en charge de nouveaux formats audio pour la transcription (SRT, VTT) et amélioration de la transcription audio avec la prise en charge de la diarisation. [#855](https://github.com/etalab-ia/OpenGateLLM/issues/855), [#832](https://github.com/etalab-ia/OpenGateLLM/issues/832)
- Correction d'un bug empêchant la fermeture correcte des fichiers PDF après lecture. [#833](https://github.com/etalab-ia/OpenGateLLM/issues/833)
- Amélioration de l'interface utilisateur du playground avec des corrections mineures. [#860](https://github.com/etalab-ia/OpenGateLLM/issues/860)
- Correction de la gestion du contenu non-string renvoyé par l'API Mistral. [#892](https://github.com/etalab-ia/OpenGateLLM/issues/892)

### Évolutions techniques
- Refactorisation de l'endpoint `/v1/admin/users` pour une meilleure architecture. [#867](https://github.com/etalab-ia/OpenGateLLM/issues/867)
- Refactorisation du code lié à la récupération des modèles, en séparant la logique en deux use cases distincts. [#890](https://github.com/etalab-ia/OpenGateLLM/issues/890)
- Renommage de `userinforepo` pour une meilleure clarté du code. [#865](https://github.com/etalab-ia/OpenGateLLM/issues/865)
- Injection du contexte dans Langfuse pour une meilleure traçabilité. [#889](https://github.com/etalab-ia/OpenGateLLM/issues/889)
- Correction de l'URL de base pour Langfuse. [#868](https://github.com/etalab-ia/OpenGateLLM/issues/868)
- Création d'une image Docker privée pour le playground afin d'améliorer la sécurité. [#835](https://github.com/etalab-ia/OpenGateLLM/issues/835)
- Corrections et améliorations du workflow de déploiement et de la documentation. [#857](https://github.com/etalab-ia/OpenGateLLM/issues/857), [#837](https://github.com/etalab-ia/OpenGateLLM/issues/837), [#836](https://github.com/etalab-ia/OpenGateLLM/issues/836)

### Autres changements
- Mise à jour de la documentation générée automatiquement et des versions de publication. [#891](https://github.com/etalab-ia/OpenGateLLM/issues/891), [#862](https://github.com/etalab-ia/OpenGateLLM/issues/862), [#858](https://github.com/etalab-ia/OpenGateLLM/issues/858), [#838](https://github.com/etalab-ia/OpenGateLLM/issues/838)
- Ignorer certaines vulnérabilités (CVE) dans les scans de sécurité Trivy. [#874](https://github.com/etalab-ia/OpenGateLLM/issues/874), [#873](https://github.com/etalab-ia/OpenGateLLM/issues/873), [#872](https://github.com/etalab-ia/OpenGateLLM/issues/872)
- Renommage du fichier `bootstrapadmin`. [#864](https://github.com/etalab-ia/OpenGateLLM/issues/864)
- Ajout d'un nouveau document à la documentation déployée dans le playground. [#854](https://github.com/etalab-ia/OpenGateLLM/issues/854)
- Mise à jour des dépendances Astro et Node. [#840](https://github.com/etalab-ia/OpenGateLLM/issues/840)
