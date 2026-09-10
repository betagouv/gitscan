## Changelog : egapro (30 derniers jours, au 09 septembre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes avec le lancement de l'observatoire public et une amélioration significative du parcours de déclaration (rémunération, CSE et gestion des effectifs). Les évolutions se sont concentrées sur la mise en conformité avec les maquettes de design, l'amélioration de l'accessibilité et le renforcement de la robustesse technique de l'API.

### Évolutions fonctionnelles

**Déclarations et parcours de conformité**
- Mise en place de la "représentation équilibrée" pour les entreprises de moins de 1000 salariés [#4364](https://github.com/SocialGouv/egapro/issues/4364).
- Amélioration de la déclaration de rémunération : gestion des effectifs par base de rémunération [#4325], [#4384], ajout de colonnes pour l'import des catégories [#4387] et renforcement des contrôles sur les quartiles [#4317].
- Optimisation du parcours CSE : suppression de questions redondantes [#4444], [#4441], [#4436] et gestion améliorée du dépôt d'avis [#4439].
- Amélioration de la gestion des effectifs : intégration de l'effectif physique par base de rémunération [#4391] et correction de l'affichage des données pour les entreprises de moins de 50 salariés [#4365].

**Mon espace et profil**
- Ajout de badges d'état pour les démarches (Clôturée - incomplète / non effectuée) [#4442](https://github.com/SocialGouv/egapro/issues/4442).
- Affichage d'un bandeau pays pour les entreprises étrangères [#4427](https://github.com/SocialGouv/egapro/issues/4427).
- Refonte de l'interface "Mon profil" et du panneau de gestion pour une meilleure conformité aux maquettes (alignements, messages d'erreur et mentions d'obligation) [#4188], [#4313], [#4320].
- Nettoyage de l'interface : retrait du fil d'Ariane dans l'espace personnel [#4316] et masquage du bandeau des archives [#4199].

**Observatoire et données entreprises**
- Lancement de l'observatoire public [#4360](https://github.com/SocialGouv/egapro/issues/4360).
- Amélioration de la fiabilité des données entreprises : intégration du code NAF dans les libellés [#4446], remontée des entreprises cessées du registre [#4394] et gestion du mapping pays [#4396].

**Corrections UI/UX et communications**
- Amélioration des accusés de réception par email pour les différentes étapes de déclaration [#4433], [#4431], [#4241].
- Corrections d'affichage et de mise en page : alignement des éléments selon les maquettes Figma, gestion des titres orphelins dans les PDF [#4257], et corrections des espacements dans les formulaires [#4144], [#4147].

### Évolutions techniques

**Architecture et API**
- Refactorisation de l'API : centralisation des routes statiques [#4484], mutualisation du contrôle de verrou REST [#4472] et création d'un helper partagé pour la gestion des sessions [#4477].
- Amélioration de la robustesse de tRPC via l'utilisation de types dérivés et de schémas Zod par routeur [#4481].
- Renforcement de l'auditabilité du système par l'intégration de la couverture `withAuditedRoute` sur les route handlers de l'API [#4480].

**CI/CD et Tests**
- Optimisation des pipelines de CI : gestion améliorée des branches de test [#4423] et automatisation de la validation des dépendances [#4366].
- Amélioration de la suite de tests E2E (Playwright) pour réduire les délais d'installation des dépendances [#4270].
- Migration de l'outil de test de messagerie de MailDev vers Mailpit pour l'environnement Atlas [#4429].

### Autres changements

**Accessibilité et Documentation**
- Mise à jour et migration des outils d'accessibilité (Ultra11y) vers le référentiel SocialGouv [#4454], [#4407], [#4169].
- Ajout de guides d'utilisation pour le dépôt Codex [#4367].
- Mise à jour du versioning de l'application dans le pied de page [#4139].
