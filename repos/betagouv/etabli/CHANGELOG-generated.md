## Changelog : etabli (30 derniers jours, au 14 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent principalement sur l'assistant conversationnel, avec des optimisations de performance, une meilleure qualité des réponses et une correction de bugs. Des améliorations ont également été apportées à la recherche d'initiatives, à l'interface utilisateur et à l'infrastructure sous-jacente.

### Évolutions fonctionnelles
- L'assistant conversationnel utilise désormais un modèle français plus petit pour des réponses plus rapides. La longueur des réponses est ajustée en fonction des documents pertinents.
- Amélioration de la recherche d'initiatives :
    - Possibilité de sélectionner une page spécifique dans les résultats de recherche au lieu de simplement naviguer avec "précédent/suivant" [#25a04f5](https://github.com/betagouv/etabli/pulls/25a04f5).
    - Ajout de filtres sur les propriétés des initiatives et utilisation des paramètres d'URL pour la recherche [#df88c61](https://github.com/betagouv/etabli/pulls/df88c61).
- Amélioration de l'interface utilisateur :
    - Simplification de l'étape d'exploration pour mieux diriger les utilisateurs vers les deux modes de recherche.
    - Amélioration de l'ergonomie des cartes d'initiatives.
    - Correction de l'affichage des soulignements sur certains liens.
- L'assistant conversationnel gère mieux les questions de suivi en conservant l'historique des initiatives précédentes [#12e1e312](https://github.com/betagouv/etabli/pulls/1e1e312).
- L'assistant conversationnel affiche plus souvent un conseil d'utilisation [#a79b3a8](https://github.com/betagouv/etabli/pulls/a79b3a8).

### Évolutions techniques
- Mise à jour du modèle Mistral utilisé par l'assistant conversationnel pour bénéficier de nouvelles capacités [#4d7838d](https://github.com/betagouv/etabli/pulls/4d7838d).
- Changement de la stratégie de recherche pour l'assistant, passant à une recherche lexicale pour de meilleurs résultats dans le répertoire [#6c66153](https://github.com/betagouv/etabli/pulls/6c66153).
- Mise à jour de Prisma vers la version 7 [#68a0adc](https://github.com/betagouv/etabli/pulls/68a0adc).
- Amélioration de la gestion des sauvegardes de la base de données pour éviter les blocages [#28f7316](https://github.com/betagouv/etabli/pulls/28f7316).
- Optimisation des tests unitaires et de Storybook pour améliorer les performances [#79d7be8](https://github.com/betagouv/etabli/pulls/79d7be8) et [#a03d02b](https://github.com/betagouv/etabli/pulls/a03d02b).
- Simplification des étapes de CI/CD [#f9af7fe](https://github.com/betagouv/etabli/pulls/f9af7fe).
- Correction d'une erreur de décodage HTTP en production [#f05255b](https://github.com/betagouv/etabli/pulls/f05255b) et [#6111280](https://github.com/betagouv/etabli/pulls/6111280).

### Autres changements
- Correction d'un problème empêchant le déploiement sur Clever Cloud [#41c3ea2](https://github.com/betagouv/etabli/pulls/41c3ea2).
- Mise à jour de la version de Node.js attendue par `mise` [#0d10a4a](https://github.com/betagouv/etabli/pulls/0d10a4a).
- Correction de problèmes liés à l'utilisation de certificats SSL auto-signés avec Prisma v7 [#bf0adce](https://github.com/betagouv/etabli/pulls/bf0adce).
- Correction d'un problème de nettoyage des fragments de données [#941f7f8](https://github.com/betagouv/etabli/pulls/941f7f8).
- Correction d'une erreur de runtime liée à Prisma [#85ea63d](https://github.com/betagouv/etabli/pulls/85ea63d).
- Amélioration du script de démarrage [#1904857](https://github.com/betagouv/etabli/pulls/1904857).
- Correction d'un bug où l'assistant ne trouvait pas certaines initiatives [#c84a24e](https://github.com/betagouv/etabli/pulls/c84a24e).
- Correction d'un problème de mémoire avec le nouveau modèle français de l'assistant [#097ba64](https://github.com/betagouv/etabli/pulls/097ba64).
- Le modèle de reranking LLM a été mis à jour pour le français [#a154b38](https://github.com/betagouv/etabli/pulls/a154b38).
- Correction d'un problème d'importation de packages dans le CLI [#14fe314](https://github.com/betagouv/etabli/pulls/14fe314).
- Correction d'un code d'erreur HTTP incorrect lors de la recherche d'initiatives inexistantes [#827fb73](https://github.com/betagouv/etabli/pulls/827fb73).
- Mise à jour de la version de la base de données sur le provider [#7dd7e2f](https://github.com/betagouv/etabli/pulls/7dd7e2f).
