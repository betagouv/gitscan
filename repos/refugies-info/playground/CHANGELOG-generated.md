## Changelog : playground (30 derniers jours, au 08/10/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la stabilisation du workflow de traduction et l'amélioration de la réactivité de l'équipe grâce à l'intégration de notifications Slack. Parallèlement, une phase importante de préparation technique a été entamée pour la migration de l'infrastructure d'intelligence artificielle (agents) afin de garantir une transition fluide et une meilleure qualité de génération.

### Évolutions fonctionnelles
- **Amélioration du suivi des traductions** : Correction des problèmes de publication et de gestion des statuts après une régénération par l'IA ([#346](https://github.com/refugies-info/playground/pull/346), [#343](https://github.com/refugies-info/playground/pull/343)).
- **Nouvelles informations et visibilité** : Ajout de la date de publication dans les tableaux de bord ([#335](https://github.com/refugies-info/playground/pull/335)), amélioration de l'affichage des liens externes et correction de la visibilité des enregistrements publiés pour les traducteurs ([#341](https://github.com/refugies-info/playground/pull/341)).
- **Système d'alertes** : Mise en place de notifications Slack pour signaler les échecs de traduction et l'état de fin des processus d'intégration continue ([#351](https://github.com/refugies-info/playground/pull/351)).

### Évolutions techniques
- **Optimisation de l'IA (LLM)** : Forçage du modèle sur Letta pour corriger des problèmes de qualité de traduction ([#349](https://github.com/refugies-info/playground/pull/349)) et enregistrement systématique du modèle utilisé dans les rapports de l'agent ([#342](https://github.com/refugies-info/playground/pull/342)).
- **Préparation de la migration des agents** : Durcissement de l'interface API Letta v1 en prévision de la migration vers le nouveau SDK ([#340](https://github.com/refugies-info/playground/pull/340)) et planification de la transition technique.
- **Base de données et traçabilité** : Ajout du champ `origin_id` pour améliorer la traçabilité des données lors des envois de webhooks ([#337](https://github.com/refugies-info/playground/pull/337)).
- **CI/CD** : Optimisation des workflows de revue de code et stabilisation des déclencheurs de tests.

### Autres changements
- **Documentation** : Rédaction approfondie du plan de migration des agents et ajout d'une documentation sur les conventions de codage ([#328](https://github.com/refugies-info/playground/pull/328)).
- **Maintenance** : Nettoyage de la configuration du workspace (pnpm) et des scripts d'enregistrement d'outils.
