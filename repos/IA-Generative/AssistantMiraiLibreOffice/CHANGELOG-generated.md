## Changelog : AssistantMiraiLibreOffice (30 derniers jours, au 06 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives au mécanisme de mise à jour de l'extension, le rendant plus robuste et plus facile à diagnostiquer en cas de problème. Des corrections ont également été apportées à l'authentification SSO et à la gestion des configurations. Enfin, un bouton "Ouvrir le dossier" a été ajouté pour faciliter le débogage et le test local de l'extension.

### Évolutions fonctionnelles
- Ajout d'un bouton "Ouvrir le dossier" dans la boîte de dialogue de mise à jour bloquée, permettant d'ouvrir le dossier de l'extension dans l'explorateur de fichiers natif ([#7](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/7)).
- Amélioration de la gestion des erreurs lors de la mise à jour, avec un message plus clair en cas d'échec et des instructions pour une installation manuelle.
- Mise en place d'un mécanisme de dégradation propre en cas d'échec de la mise à jour automatique, évitant les boucles infinies.
- Correction de l'authentification SSO pour les profils "int" utilisant Keycloak et MySSO ([#2](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/2), [#3](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/3)).

### Évolutions techniques
- Refonte du mécanisme de mise à jour : installation "in-process" via `ExtensionManager`, redémarrage natif de LibreOffice, et gestion du failover de téléchargement ([#16](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/16), [#18](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/18), [#19](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/19)).
- Amélioration de la robustesse du téléchargement des mises à jour avec un mécanisme de failover multi-bootstrap et la gestion de l'URL de bootstrap précédente fonctionnelle ([#16](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/16)).
- Optimisation de la récupération de la configuration avec un système de cache-first, un timeout court et un failover intelligent ([#3](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/3)).
- Utilisation de `ExtensionManager.get()` pour accéder à l'instance singleton de `ExtensionManager` ([#14](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/14), [#15](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/15)).
- Correction d'un problème où l'ancienne version de l'extension n'était pas supprimée avant l'installation de la nouvelle ([#17](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/17)).

### Autres changements
- Mise à jour de la documentation concernant le mécanisme de mise à jour ([#11](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/11), [#18](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/18)).
- Ajout d'un guide pour les développeurs.
- Amélioration des tests et de l'hygiène du code.
- Mises à jour de la configuration pour supporter les profils transport-only et SSO autoritatif DM.
- Bump de version : 0.0.1.0.14 -> 0.0.1.0.22.
