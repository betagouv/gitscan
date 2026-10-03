## Changelog : euphrosyne (30 derniers jours, au 01/10/2026)

### Résumé
Les récentes évolutions se sont concentrées sur le renforcement de la sécurité des accès, notamment via l'amélioration du système d'authentification ORCID et une gestion plus stricte des permissions sur l'API. Le projet a également amélioré la gestion des invitations utilisateurs et mis à jour ses engagements en matière d'accessibilité numérique.

### Évolutions fonctionnelles
- **Authentification et invitations** : Amélioration du processus d'inscription via ORCID pour garantir une liaison correcte entre les nouveaux comptes et les invitations validées [#2034](https://github.com/betagouv/euphrosyne/pull/2034).
- **Gestion des utilisateurs** : Correction d'un problème affectant le statut "staff" des nouveaux utilisateurs invités à rejoindre un projet [#2033](https://github.com/betagouv/euphrosyne/pull/2033).
- **Accessibilité** : Mise à jour de la page statique de déclaration d'accessibilité du site [#2022](https://github.com/betagouv/euphrosyne/pull/2022).

### Évolutions techniques
- **Sécurité de l'API** : Renforcement de la sécurité en imposant l'application des permissions de projet sur l'ensemble des routes de l'API [#2035](https://github.com/betagouv/euphrosyne/pull/2035).
- **Refactorisation de l'authentification** : Migration du flux ORCID vers l'utilisation native de `social-django` pour une meilleure stabilité [#2034](https://github.com/betagouv/euphrosyne/pull/2034).
- **Automatisation CI/CD** : 
    - Mise en place de l'auto-fusion (automerge) pour les mises à jour de dépendances via Dependabot [#2016](https://github.com/betagouv/euphrosyne/pull/2016).
    - Amélioration de la robustesse de la chaîne d'intégration continue (CI) avec des contrôles de types plus stricts et une normalisation des traductions.

### Autres changements
- **Documentation** : Ajout de la documentation concernant la génération des traductions et nettoyage de références obsolètes dans le README.
