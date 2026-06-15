## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans la gestion des locataires et des garanties, ainsi que sur la robustesse des tests automatisés. Des corrections ont été apportées pour améliorer la clarté et la fiabilité du processus de saisie des informations. L'ajout d'une analyse de résidence et d'un fichier `robot.txt` pour le propriétaire améliorent également la plateforme.

### Évolutions fonctionnelles
- Ajout d'un bouton de suppression de garant sur la page de validation. [#1966](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1966)
- Amélioration de l'analyse de la résidence avec ajout d'une nouvelle étape. [#1971](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1971)
- Correction d'un bug empêchant le bouton de l'étape de résidence d'être désactivé correctement. [#1972](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1972)
- Amélioration de l'affichage de l'année de l'avis d'imposition pour la rente viagère et la pension. [#1968](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1968) et [#1974](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1974)
- Ajout d'un compteur de caractères pour le message de filigrane. [#1977](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1977)
- Correction de l'envoi de l'email du co-locataire à l'API lorsque les noms sont déjà enregistrés. [#1934](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1934)
- Ajout d'un message d'erreur toast pour le texte personnalisé dépassant la longueur maximale. [#1969](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1969)
- Correction de l'affichage du message de clarification du co-locataire. [#1975](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1975)
- Masquage du message de clarification lorsque le locataire est de type "JOIN". [#1973](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1973)
- Amélioration de l'accessibilité avec une déclaration a11y. [#1980](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1980)

### Évolutions techniques
- Amélioration des messages et des artefacts vidéo dans les tests E2E. [#1970](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1970)
- Correction pour éviter l'exécution concurrente des jobs E2E. [#1984](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1984)
- Ajout d'un fichier `robot.txt` pour le propriétaire. [#1965](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1965)
- Suppression des retours à la ligne dans le `customText` avant la soumission du formulaire. [#1976](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1976)
- Ajout d'un scénario E2E pour un cas de refus. [#1985](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1985)

### Autres changements
- Ajout d'un fichier `agent.md`. [#1981](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1981)
- Bump de version à V3.5.10 et V3.5.11.
- Correction de la marge supérieure du bouton de suppression du garant. [#1967](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1967)
