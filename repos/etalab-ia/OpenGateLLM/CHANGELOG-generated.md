## Changelog : OpenGateLLM (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'architecture interne d'OpenGateLLM, notamment au niveau de la gestion des rôles et des modèles. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant la transcription audio et les formulaires dans l'interface de test. La sécurité a été renforcée avec l'ajout d'outils d'analyse de vulnérabilités.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'envoi du code de langue par défaut au modèle Whisper lors de la transcription audio. [#819](https://github.com/etalab-ia/OpenGateLLM/issues/819)
- Correction d'un bug dans l'interface de test (playground) où la longueur maximale du mot de passe était incorrectement limitée à 72 caractères. [#809](https://github.com/etalab-ia/OpenGateLLM/issues/809)
- Correction de l'affichage des valeurs non affichées dans les formulaires de l'interface de test (provider, router, user). [#802](https://github.com/etalab-ia/OpenGateLLM/issues/802)
- Correction d'un bug empêchant le filtrage correct des collections via l'API. [#789](https://github.com/etalab-ia/OpenGateLLM/issues/789)
- Ajout de la compatibilité avec la signature héritée de l'utilisation des impacts. [#791](https://github.com/etalab-ia/OpenGateLLM/issues/791)

### Évolutions techniques
- Refactorisation de la gestion des rôles pour adopter une architecture plus propre et plus maintenable. Les endpoints d'administration des rôles ont été revus et simplifiés. [#821](https://github.com/etalab-ia/OpenGateLLM/issues/821), [#817](https://github.com/etalab-ia/OpenGateLLM/issues/817), [#808](https://github.com/etalab-ia/OpenGateLLM/issues/808), [#801](https://github.com/etalab-ia/OpenGateLLM/issues/801)
- Refactorisation de la classe `BaseModelProvider` pour améliorer la structure du code. [#796](https://github.com/etalab-ia/OpenGateLLM/issues/796)
- Dissociation de la clé de chiffrement des clés API du mot de passe maître pour une meilleure sécurité. [#779](https://github.com/etalab-ia/OpenGateLLM/issues/779)
- Ajout de l'outil Trivy pour l'analyse des vulnérabilités dans la chaîne d'approvisionnement. [#793](https://github.com/etalab-ia/OpenGateLLM/issues/793)
- Ajout de règles Semgrep pour l'analyse statique du code et l'amélioration de la sécurité. [#794](https://github.com/etalab-ia/OpenGateLLM/issues/794), [#797](https://github.com/etalab-ia/OpenGateLLM/issues/797)
- Nettoyage des schémas de modèles (provider et routers) pour une meilleure lisibilité et maintenabilité. [#783](https://github.com/etalab-ia/OpenGateLLM/issues/783)

### Autres changements
- Mise à jour de la documentation générée et des versions de publication. [#795](https://github.com/etalab-ia/OpenGateLLM/issues/795)
- Correction de la racine de scan invalide pour Semgrep. [#797](https://github.com/etalab-ia/OpenGateLLM/issues/797)
- Correction du code de langue par défaut pour la transcription audio, passant de "english" à "en". [#807](https://github.com/etalab-ia/OpenGateLLM/issues/807)
