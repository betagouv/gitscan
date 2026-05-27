## Changelog : mon-entreprise (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la précision des calculs pour les auto-entrepreneurs, la correction de vulnérabilités de sécurité dans les dépendances, et l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'une fiche de paie pour les SASU et des améliorations sur le questionnaire salarié. Des refactorings importants ont également été réalisés pour améliorer la maintenabilité du code et la robustesse de la simulation.

### Évolutions fonctionnelles
- Ajout d'une fiche de paie pour les SASU, incluant les cotisations et le calcul du net à payer. [#6de725e](https://github.com/betagouv/mon-entreprise/commit/6de725e)
- Amélioration du questionnaire pour les salariés avec une liste de questions fixée et un réordonnancement des raccourcis. [#da62f90](https://github.com/betagouv/mon-entreprise/commit/da62f90), [#078441e](https://github.com/betagouv/mon-entreprise/commit/078441e)
- Correction du calcul de l'IR (Impôt sur le Revenu) pour les auto-entrepreneurs. [#3670b6d](https://github.com/betagouv/mon-entreprise/commit/3670b6d)
- Ajout de l'Acre au montant net social pour les MNS. [#76cd844](https://github.com/betagouv/mon-entreprise/commit/76cd844)
- Correction de la présentation des frais professionnels dans la fiche de paie des salariés. [#9196de7](https://github.com/betagouv/mon-entreprise/commit/9196de7)
- Correction de l'ordre des questions dans le questionnaire, notamment lorsque l'ordre est imposé. [#a578234](https://github.com/betagouv/mon-entreprise/commit/a578234)
- Ajout de la cotisation Apec pour les SASU. [#be518df](https://github.com/betagouv/mon-entreprise/commit/be518df)
- Suppression des frais professionnels de la rémunération brute pour les SASU. [#bb4fae1](https://github.com/betagouv/mon-entreprise/commit/bb4fae1)

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (Koa, happy-dom, handlebars, form-data, axios, protobufjs, crisp-api, storybook, cypress). [#d0b0b68](https://github.com/betagouv/mon-entreprise/commit/d0b0b68), [#bcff703](https://github.com/betagouv/mon-entreprise/commit/bcff703), [#776a76f](https://github.com/betagouv/mon-entreprise/commit/776a76f), [#64bdcb5](https://github.com/betagouv/mon-entreprise/commit/64bdcb5), [#4fc3d93](https://github.com/betagouv/mon-entreprise/commit/4fc3d93), [#46158a5](https://github.com/betagouv/mon-entreprise/commit/46158a5), [#18e60aa](https://github.com/betagouv/mon-entreprise/commit/18e60aa), [#04fb200](https://github.com/betagouv/mon-entreprise/commit/04fb200)
- Refactor de la gestion des règles d'identité de l'entreprise pour améliorer la robustesse de la simulation. [#4453998](https://github.com/betagouv/mon-entreprise/commit/4453998), [#65ec594](https://github.com/betagouv/mon-entreprise/commit/65ec594), [#6595a87](https://github.com/betagouv/mon-entreprise/commit/6595a87)
- Amélioration de la gestion des erreurs dans la simulation, notamment en évitant de vider toute la situation en cas d'erreur sur une règle spécifique. [#ab25831](https://github.com/betagouv/mon-entreprise/commit/ab25831), [#bb40ba9](https://github.com/betagouv/mon-entreprise/commit/bb40ba9), [#ebdde02](https://github.com/betagouv/mon-entreprise/commit/ebdde02)
- Migration vers Next.js 16 et implémentation de l'internationalisation (i18n) côté serveur (SSR). [#115ad14](https://github.com/betagouv/mon-entreprise/commit/115ad14)
- Refactor de la fiche de paie pour améliorer la lisibilité et la maintenabilité du code. [#c099998](https://github.com/betagouv/mon-entreprise/commit/c099998), [#b917f26](https://github.com/betagouv/mon-entreprise/commit/b917f26), [#ad6437c](https://github.com/betagouv/mon-entreprise/commit/ad6437c), [#7cd1d4e](https://github.com/betagouv/mon-entreprise/commit/7cd1d4e)

### Autres changements
- Correction de quelques erreurs de traduction dans la fiche de paie. [#c2a43c2](https://github.com/betagouv/mon-entreprise/commit/c2a43c2), [#0b31910](https://github.com/betagouv/mon-entreprise/commit/0b31910)
- Correction d'un bug dans l'iframe qui ignorait incorrectement certaines règles. [#9a53c13](https://github.com/betagouv/mon-entreprise/commit/9a53c13)
- Amélioration du pipeline CI/CD pour Algolia, avec une meilleure isolation des étapes et une simplification du processus de déploiement. [#e28a8a8](https://github.com/betagouv/mon-entreprise/commit/e28a8a8), [#daf4cc8](https://github.com/betagouv/mon-entreprise/commit/daf4cc8), [#cd3756b](https://github.com/betagouv/mon-entreprise/commit/cd3756b)
- Suppression de code commenté inutile. [#3505989](https://github.com/betagouv/mon-entreprise/commit/3505989)
- Correction de linter. [#a19f1b4](https://github.com/betagouv/mon-entreprise/commit/a19f1b4)
- Correction d'une erreur d'envoi de l'échec de chargement Piano Analytics à Sentry. [#b306680](https://github.com/betagouv/mon-entreprise/commit/b306680)
- Traduction de la page d'accueil "hello world". [#f496d1c](https://github.com/betagouv/mon-entreprise/commit/f496d1c)
