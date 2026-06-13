## Changelog : etabli (30 derniers jours, au 13 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'assistant conversationnel, la recherche d'initiatives et la stabilité de la plateforme. L'assistant a été optimisé pour une meilleure compréhension des requêtes et une recherche plus pertinente. La recherche a également été améliorée avec l'ajout de filtres et une meilleure gestion des résultats. Des corrections ont été apportées pour résoudre des problèmes de déploiement et de performance.

### Évolutions fonctionnelles
- Amélioration de l'assistant :
    - L'assistant prend désormais en compte l'historique des initiatives lors des questions suivantes [#38d7c25](https://github.com/betagouv/etabli/commit/38d7c25).
    - Amélioration de la qualité des réponses de l'assistant grâce à la mise à jour du modèle Mistral utilisé [#4d7838d](https://github.com/betagouv/etabli/commit/4d7838d).
    - L'assistant utilise désormais une recherche lexicale pour améliorer la pertinence des résultats [#6c66153](https://github.com/betagouv/etabli/commit/6c66153).
    - Correction d'un problème empêchant l'assistant de retrouver certaines initiatives [#c84a24e](https://github.com/betagouv/etabli/commit/c84a24e).
- Recherche :
    - Ajout de filtres sur les propriétés des initiatives pour affiner les recherches [#df88c61](https://github.com/betagouv/etabli/commit/df88c61).
    - Possibilité de naviguer entre les pages de résultats de recherche avec des boutons "Précédent" et "Suivant" [#25a04f5](https://github.com/betagouv/etabli/commit/25a04f5).
    - Amélioration de l'interface des cartes d'initiatives pour une meilleure lisibilité [#5d933a0](https://github.com/betagouv/etabli/commit/5d933a0).
- Navigation :
    - Retour d'un code d'erreur 404 approprié si une initiative n'est pas trouvée [#827fb73](https://github.com/betagouv/etabli/commit/827fb73).

### Évolutions techniques
- Mise à jour de Prisma vers la version 7 [#68a0adc](https://github.com/betagouv/etabli/commit/68a0adc).
- Amélioration du CI/CD :
    - Simplification des étapes du pipeline CI [#f9af7fe](https://github.com/betagouv/etabli/commit/f9af7fe).
    - Correction d'un problème de déploiement sur Clever Cloud [#41c3ea2](https://github.com/betagouv/etabli/commit/41c3ea2).
    - Ajout d'une tentative de résolution d'une erreur de décodage HTTP en production [#f05255b](https://github.com/betagouv/etabli/commit/f05255b).
- Tests :
    - Utilisation de workers pour paralléliser les tests et améliorer la performance [#836fda9](https://github.com/betagouv/etabli/commit/836fda9).
    - Amélioration de la performance des tests Storybook [#a03d02b](https://github.com/betagouv/etabli/commit/a03d02b).
    - Utilisation d'une librairie de test plus performante pour Storybook [#79d7be8](https://github.com/betagouv/etabli/commit/79d7be8).
- Infrastructure :
    - Correction d'un problème avec les sauvegardes de la base de données qui bloquaient les clients [#28f7316](https://github.com/betagouv/etabli/commit/28f7316).
    - Mise à jour de la version de PostgreSQL sur le provider [#7dd7e2f](https://github.com/betagouv/etabli/commit/7dd7e2f).

### Autres changements
- Correction d'un problème empêchant la modification du champ de saisie de l'assistant lors de la soumission [#7f00201](https://github.com/betagouv/etabli/commit/7f00201).
- Amélioration du prompt système de l'assistant [#938e5fd](https://github.com/betagouv/etabli/commit/938e5fd).
- Ajout d'un conseil d'utilisation de l'assistant plus fréquemment [#a79b3a8](https://github.com/betagouv/etabli/commit/a79b3a8).
- Correction d'un problème lié à l'utilisation de certificats SSL auto-signés avec Prisma v7 [#bf0adce](https://github.com/betagouv/etabli/commit/bf0adce).
- Correction d'un problème lié à la gestion des fragments tagués et non tagués [#941f7f8](https://github.com/betagouv/etabli/commit/941f7f8).
- Correction d'une erreur de runtime liée à Prisma [#85ea63d](https://github.com/betagouv/etabli/commit/85ea63d).
- Correction de problèmes d'affichage des soulignements sur certains liens [#ca661b7](https://github.com/betagouv/etabli/commit/ca661b7).
- Mise à jour de la version de Node.js attendue par `mise` [#0d10a4a](https://github.com/betagouv/etabli/commit/0d10a4a).
