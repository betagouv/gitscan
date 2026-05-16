## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'indexation et de l'évaluation des documents, ainsi que sur la sécurité et la gestion des dépendances. De nouvelles fonctionnalités permettent la gestion de documents "maîtrisés" (questions/réponses) et l'utilisation d'OCR via Docling. Des corrections ont été apportées pour améliorer la robustesse et la fiabilité du système.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer des documents indexés. [#44a5bf3](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/44a5bf3)
- Implémentation d'une route POST `/documents` pour l'indexation de documents. [#a59d534](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/a59d534)
- Ajout d'une route POST `/evaluation` pour lancer une évaluation. [#53b8f3a](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/53b8f3a)
- Possibilité de passer les fichiers d'évaluation et de mapping en argument à `evaluateur_mqc`. [#33efb0d](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/33efb0d)
- Introduction de la gestion de documents contenant des questions/réponses maîtrisées, avec la possibilité de les indexer et de les ajouter à une collection. [#ff400c9](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/ff400c9)
- Intégration d'un appel à un VLM (Vision Language Model) via ALBERT pour effectuer de l'OCR (reconnaissance optique de caractères) via Docling. [#e93409e](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/e93409e)
- Ajout d'un dataset contenant tous les documents. [#471295a](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/471295a)

### Évolutions techniques
- Implémentation d'un *cooldown* d'une semaine pour l'installation des dépendances afin d'améliorer la sécurité. [#a7dd503](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/a7dd503)
- L'indexation et l'évaluation sont maintenant exécutées dans des tâches en arrière-plan pour améliorer la réactivité de l'API. [#d0a1b78](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/d0a1b78) et [#b98730a](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/b98730a)
- Correction d'une erreur de déploiement due à une dépendance manquante (pilote Postgres). [#6350851](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/6350851)
- Renforcement du prompt pour interdire les questions relatives aux Rx. [#b83f216](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/b83f216)
- Suppression de la notion de score de similarité. [#0650eee](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/0650eee)
- Amélioration de la gestion des erreurs lors de l'évaluation, avec journalisation des erreurs d'origine. [#ab118ff](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/ab118ff)
- Vérification de la signature du token JWT et fourniture du secret JWT en paramètre. [#ad2d80b](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/ad2d80b) et [#151a83b](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/151a83b)

### Autres changements
- Correction de bugs et améliorations de la sortie de `deepeval`. [#5c38282](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/5c38282), [#b5871b0](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/b5871b0), [#46b4596](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/46b4596)
- Slugification de la question de la réponse maîtrisée. [#da04f69](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/da04f69)
- Refactoring du code pour introduire des documents contenant des questions/réponses maîtrisées. [#afdd7c6](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/afdd7c6)
- Ajout d'un fichier de configuration minimal pour Renovate. [#4e0b91d](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/4e0b91d)
- Les documents sont maintenant "jeopardisés" une fois indexés. [#cd27315](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/cd27315)
- Correction d'un problème où l'exécution de `document_existe` et `supprime_document` pouvait interrompre le traitement. [#c05c69d](https://github.com/betagouv/anssi-recommandations-cyber-data/issues/c05c69d)
