## Changelog : OpenGateLLM (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'architecture interne d'OpenGateLLM, notamment au niveau de la gestion des rôles et des modèles. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant l'audio et le playground. Des améliorations de la sécurité ont été intégrées avec l'ajout de nouvelles règles Semgrep et l'intégration de Trivy pour la sécurité de la chaîne d'approvisionnement.

### Évolutions fonctionnelles
- Correction d'un bug dans le playground où le mot de passe ne pouvait pas dépasser 72 caractères [#809](https://github.com/etalab-ia/OpenGateLLM/issues/809).
- Correction du code de langue par défaut pour la transcription audio, passant de "english" à "en" [#807](https://github.com/etalab-ia/OpenGateLLM/issues/807).
- Correction d'un bug d'affichage des valeurs dans les formulaires du playground (provider, router, user) [#802](https://github.com/etalab-ia/OpenGateLLM/issues/802).
- Correction d'un bug empêchant l'envoi de la langue par défaut au modèle Whisper [#819](https://github.com/etalab-ia/OpenGateLLM/issues/819).

### Évolutions techniques
- Refactorisation importante de la gestion des rôles pour adopter une architecture plus propre et plus maintenable [#821](https://github.com/etalab-ia/OpenGateLLM/issues/821), [#817](https://github.com/etalab-ia/OpenGateLLM/issues/817), [#808](https://github.com/etalab-ia/OpenGateLLM/issues/808), [#801](https://github.com/etalab-ia/OpenGateLLM/issues/801).
- Refactorisation du `BaseModeProvider` pour une architecture plus propre [#796](https://github.com/etalab-ia/OpenGateLLM/issues/796).
- Amélioration de la gestion des URLs dans les métriques Prometheus, en utilisant des motifs de route au lieu d'URLs complètes [#824](https://github.com/etalab-ia/OpenGateLLM/issues/824).
- Dissociation de la clé de chiffrement des clés API du mot de passe maître [#779](https://github.com/etalab-ia/OpenGateLLM/issues/779).
- Ajout de Trivy pour la sécurité de la chaîne d'approvisionnement [#793](https://github.com/etalab-ia/OpenGateLLM/issues/793).

### Autres changements
- Suppression de préfixes inutiles dans les messages d'erreur [#826](https://github.com/etalab-ia/OpenGateLLM/issues/826).
- Suppression d'importations inutiles dans le domaine du modèle d'initialisation [#822](https://github.com/etalab-ia/OpenGateLLM/issues/822).
- Mise à jour de la documentation générée et des versions de publication [#795](https://github.com/etalab-ia/OpenGateLLM/issues/795).
- Ajout de règles Semgrep pour améliorer la sécurité [#794](https://github.com/etalab-ia/OpenGateLLM/issues/794).
- Correction d'un problème de racine de scan invalide avec Semgrep [#797](https://github.com/etalab-ia/OpenGateLLM/issues/797).
- Initialisation de la refactorisation de l'administration (bootstrap) [#799](https://github.com/etalab-ia/OpenGateLLM/issues/799).
