## Changelog : anssi-recommandations-cyber (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la compatibilité avec la nouvelle version de l'API Albert (0.5.0), l'amélioration de l'expérience utilisateur avec l'ajout de fonctionnalités comme la copie des sources et l'affichage de la date de mise à jour des documents, ainsi que des corrections de bugs et des optimisations de performance. Un travail important a également été réalisé sur le reclassement des sources et la gestion des documents PDF.

### Évolutions fonctionnelles
- Adaptation à l'API Albert 0.5.0 : migration des appels d'API pour utiliser les nouveaux paramètres `collection_id` et `query` au lieu de `collection` et `prompt` [#dafc362](https://github.com/betagouv/anssi-recommandations-cyber/commit/dafc362), [#a0726b9](https://github.com/betagouv/anssi-recommandations-cyber/commit/a0726b9), [#48f0221](https://github.com/betagouv/anssi-recommandations-cyber/commit/48f0221).
- Ajout d'un bouton pour copier les sources de la réponse, facilitant le partage et la vérification des informations [#be3f4c1](https://github.com/betagouv/anssi-recommandations-cyber/commit/be3f4c1).
- Affichage de la date de mise à jour du document, permettant aux utilisateurs de connaître la fraîcheur de l'information [#630019b](https://github.com/betagouv/anssi-recommandations-cyber/commit/630019b).
- Affichage du titre du document au lieu du nom du fichier [#88db2e3](https://github.com/betagouv/anssi-recommandations-cyber/commit/88db2e3).
- Amélioration de l'affichage des réponses détaillées pour une meilleure lisibilité [#f5f9b21](https://github.com/betagouv/anssi-recommandations-cyber/commit/f5f9b21).
- Ajout d'icônes DSFR aux boutons du carrousel pour une meilleure cohérence visuelle [#8abcd71](https://github.com/betagouv/anssi-recommandations-cyber/commit/8abcd71).
- Correction de la redirection de la ressource `/source` [#5aacca4](https://github.com/betagouv/anssi-recommandations-cyber/commit/5aacca4).
- Correction du nombre de résultats retournés par la recherche [#d8274e0](https://github.com/betagouv/anssi-recommandations-cyber/commit/d8274e0).
- Gestion des documents PDF : affichage en carrousel, génération d'images des pages PDF côté navigateur, affichage d'une image générique si le fichier n'est pas un PDF [#31c9674](https://github.com/betagouv/anssi-recommandations-cyber/commit/31c9674), [#10bc725](https://github.com/betagouv/anssi-recommandations-cyber/commit/10bc725), [#765b055](https://github.com/betagouv/anssi-recommandations-cyber/commit/765b055), [#992d102](https://github.com/betagouv/anssi-recommandations-cyber/commit/992d102).

### Évolutions techniques
- Intégration de `zizmor` pour la validation de la configuration, renforçant la sécurité [#e1746ed](https://github.com/betagouv/anssi-recommandations-cyber/commit/e1746ed).
- Désactivation des identifiants `git` dans les actions CI/CD pour améliorer la sécurité [#c1f0674](https://github.com/betagouv/anssi-recommandations-cyber/commit/c1f0674).
- Refactoring du code pour séparer la réponse de l'API du traitement métier [#fc6916d](https://github.com/betagouv/anssi-recommandations-cyber/commit/fc6916d).
- Intégration du reclassement par LLM et gestion des sources adaptées [#954561a](https://github.com/betagouv/anssi-recommandations-cyber/commit/954561a), [#53fd298](https://github.com/betagouv/anssi-recommandations-cyber/commit/53fd298), [#805cfd3](https://github.com/betagouv/anssi-recommandations-cyber/commit/805cfd3).
- Suppression du feature flag `reclassement` [#8a62645](https://github.com/betagouv/anssi-recommandations-cyber/commit/8a62645).

### Autres changements
- Sécurisation du vocabulaire à portée juridique du prompt [#c6ec901](https://github.com/betagouv/anssi-recommandations-cyber/commit/c6ec901).
- Documentation sur les interactions entre MQC et Albert [#2b33f87](https://github.com/betagouv/anssi-recommandations-cyber/commit/2b33f87).
- Amélioration des tests et suppression d'éléments inutiles [#b3b67a6](https://github.com/betagouv/anssi-recommandations-cyber/commit/b3b67a6).
- Diverses mises à jour de dépendances (vitest, prettier-plugin-svelte, marked, @lab-anssi/ui-kit, dompurify, codeql-action, setup-uv, setup-python) [#bf3eec1](https://github.com/betagouv/anssi-recommandations-cyber/commit/bf3eec1), [#ef0a8f7](https://github.com/betagouv/anssi-recommandations-cyber/commit/ef0a8f7), [#ccade29](https://github.com/betagouv/anssi-recommandations-cyber/commit/ccade29), [#a00aee8](https://github.com/betagouv/anssi-recommandations-cyber/commit/a00aee8), [#4a6ab47](https://github.com/betagouv/anssi-recommandations-cyber/commit/4a6ab47), [#7437b26](https://github.com/betagouv/anssi-recommandations-cyber/commit/7437b26), [#d35da4b](https://github.com/betagouv/anssi-recommandations-cyber/commit/d35da4b), [#97c2949](https://github.com/betagouv/anssi-recommandations-cyber/commit/97c2949).
