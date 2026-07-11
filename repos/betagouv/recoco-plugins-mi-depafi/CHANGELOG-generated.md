## Changelog : recoco-plugins-mi-depafi (30 derniers jours, au 8 juillet 2026)

### Résumé
Ce plugin, qui étend la plateforme Recommandations Collaboratives pour le Ministère de l'Intérieur, a connu des améliorations significatives en termes de gestion des réalisations, d'interface utilisateur et de structure de code. Les agents du Ministère peuvent désormais mieux gérer leurs projets de transition écologique, avec des permissions plus précises et une interface plus conviviale.

### Évolutions fonctionnelles
- Ajout de la possibilité pour les utilisateurs de modifier et supprimer leurs propres réalisations. Seul l'auteur d'une réalisation peut la modifier ou la supprimer. [#27](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/27)
- Introduction d'un indicateur visuel pour activer/désactiver des fonctionnalités (feature flags) pour faciliter les tests et le déploiement progressif. [#29](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/29)
- Amélioration de l'interface utilisateur pour l'édition de réalisations, incluant l'ajout de champs pour les chiffres clés, les documents et la date. [#26](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/26)
- Ajout d'un bouton d'édition et de suppression des réalisations pour les administrateurs. [#30](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/30)
- Mise à jour de la documentation d'installation du plugin. [#25](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/25)

### Évolutions techniques
- Refactorisation de l'architecture du projet pour une meilleure organisation des fichiers JavaScript et CSS. [#304f67c](https://github.com/betagouv/recoco-plugins-mi-depafi/commit/304f67c)
- Utilisation de `marksafe` pour la gestion de la sécurité, en accord avec le nouveau contrat de la plateforme principale. [#ddcf69f](https://github.com/betagouv/recoco-plugins-mi-depafi/commit/ddcf69f)
- Intégration de HTMX pour améliorer l'interactivité de certaines parties de l'interface. [#b70a923](https://github.com/betagouv/recoco-plugins-mi-depafi/commit/b70a923) et [#c0fa96f](https://github.com/betagouv/recoco-plugins-mi-depafi/commit/c0fa96f)
- Ajout d'un champ `created_by` à la table des réalisations pour identifier l'auteur. [#6dc0012](https://github.com/betagouv/recoco-plugins-mi-depafi/commit/6dc0012)

### Autres changements
- Correction du chemin d'accès aux ressources dans les templates. [#9abab97](https://github.com/betagouv/recoco-plugins-mi-depafi/commit/9abab97)
- Enregistrement du modèle `Realisation` dans la configuration du plugin. [#843555b](https://github.com/betagouv/recoco-plugins-mi-depafi/commit/843555b)
- Suppression d'une réversion temporaire du champ `created_by`.
- Amélioration de l'affichage des textes et des espaces dans les cartes de projet.
- Correction de l'injection des données pour l'activation des onglets.
- Suppression de l'inclusion du répertoire des données lors de la construction.
