## Changelog : lab-anssi-rula (30 derniers jours, au 25 août 2026)

### Résumé
Cette période a été marquée par une refonte majeure de l'interface utilisateur pour l'analyse des besoins et un renforcement de la fiabilité des données. L'expérience utilisateur est désormais plus encadrée grâce à un meilleur accompagnement lors de la saisie des entretiens, tandis que la robustesse du système est accrue par de nouveaux mécanismes de validation automatique.

### Évolutions fonctionnelles
- Refonte complète de l'interface utilisateur dédiée à l'analyse des besoins ([#9](https://github.com/betagouv/lab-anssi-rula/issues/9)).
- Amélioration de l'accompagnement utilisateur : affichage immédiat du guide d'utilisation et ajout d'avertissements avant l'enregistrement d'un transcript.
- Ajout de retours visuels concernant les mécanismes de sécurité (garde-fou) directement dans les formulaires.
- Amélioration de la transparence via l'ajout de liens vers les sources des correspondances.
- Corrections de bugs : résolution du problème des libellés vides dans les correspondances ([#10](https://github.com/betagouv/lab-anssi-rula/issues/10)) et correction de l'analyse pour les entretiens multiples.

### Évolutions techniques
- Implémentation d'un service de validation JSON pour sécuriser l'intégrité des transcripts.
- Optimisation de la persistance des données des transcripts lors des interactions avec l'API Albert.
- Préparation de l'infrastructure pour le déploiement d'une version de démonstration sur Clever Cloud.
- Amélioration de la qualité logicielle via la résolution de dettes techniques (*code smells*) et l'ajout d'un environnement de contrôle qualité local (*harness*).

### Autres changements
- Mise à jour de la documentation technique concernant le flux d'analyse.
