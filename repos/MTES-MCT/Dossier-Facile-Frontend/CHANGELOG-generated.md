## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans la gestion des locataires et des garanties, ainsi que sur la correction de bugs et l'amélioration de la robustesse des tests E2E. Des améliorations ont également été apportées à l'accessibilité et à la gestion des fichiers.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer un garant sur la page de validation du dossier. [#1966](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1966)
- Amélioration de l'analyse du logement et de la résidence. [#1971](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1971)
- Correction d'un bug empêchant le bouton de la page de résidence d'être désactivé correctement. [#1972](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1972)
- Amélioration de l'étiquette de l'année d'avis d'imposition pour la rente annuelle et la pension. [#1974](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1974)
- Masquage du message de clarification du co-locataire lorsque le locataire est de type "JOIN". [#1973](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1973)
- Ajout d'un compteur de caractères pour le message de filigrane. [#1977](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1977)
- Déclaration d'accessibilité (a11y). [#1980](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1980)
- Correction d'un bug où l'email du co-locataire n'était pas envoyé à l'API lorsque les noms étaient déjà enregistrés. [#1934](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1934)
- Ajout d'un message d'erreur toast pour le texte personnalisé dépassant la longueur maximale. [#1969](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1969)
- Suppression des sauts de ligne dans le texte personnalisé avant la soumission du formulaire. [#1976](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1976)

### Évolutions techniques
- Amélioration de la gestion des jobs E2E concurrents pour éviter les conflits. [#1984](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1984)
- Ajout d'un scénario E2E pour les refus. [#1985](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1985)
- Amélioration des messages Mattermost et des artefacts vidéo pour les tests E2E. [#1970](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1970)
- Ajout d'un fichier `agent.md`. [#1981](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1981)

### Autres changements
- Ajout d'un fichier `robots.txt` pour le propriétaire. [#1965](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1965)
- Corrections de style et amélioration de la marge supérieure du bouton de suppression du garant. [#1967](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1967)
- Bump de version à V3.5.10 et V3.5.11.
