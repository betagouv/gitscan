## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'analyse des documents (notamment les fiches de paie et les attestations d'assurance Visale), l'expérience utilisateur lors de la saisie des informations et la correction de bugs liés à la validation des dossiers. Plusieurs versions ont été publiées pour intégrer ces changements et améliorer la stabilité de l'application.

### Évolutions fonctionnelles
- **Analyse de documents :** Ajout de l'analyse des documents Visale pour faciliter la vérification des dossiers. [#1912](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1912)
- **Fiche de paie :**
    - Ajout d'une indication visuelle (badge d'erreur) pour signaler les problèmes lors de l'analyse de la fiche de paie. [#1947](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1947)
    - Amélioration des messages d'erreur liés à l'analyse de la fiche de paie pour une meilleure clarté. [#1940](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1940)
    - Ajout d'un support pour la compatibilité avec la règle de la feuille d'impôt. [#1946](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1946)
    - Ajout d'un callout IA pour l'analyse de la fiche de paie. [#1948](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1948)
    - Correction de l'affichage des documents lors de l'analyse de la fiche de paie. [#1949](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1949)
- **Garantie :** Correction d'un bug empêchant la validation d'un dossier avec un garant légal. [#1952](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1952)
- **Formulaire de contact :** Réinitialisation du formulaire de contact après soumission. [#1945](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1945)
- **Messages :** Masquage du bouton de réponse dans les messages une fois le dossier validé. [#1943](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1943)
- **Visale :** Amélioration de la gestion des erreurs et des messages liés à Visale. [#1926](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1926)
- **Navigation :** Remplacement du bouton "Enregistrer" par un bouton "Suivant" dans l'explication de l'analyse. [#1925](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1925)

### Évolutions techniques
- **Refactoring :** Refactorisation de la logique de sauvegarde des fichiers pour l'analyse des salaires. [#1939](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1939)
- **Tests :** Ajout de tests E2E pour la fiche de paie. [#1937](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1937)
- **Corrections diverses :** Correction de problèmes de focus et de gestion de l'état dans le formulaire de salaire. [#1941](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1941), [#1936](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1936)

### Autres changements
- Mises à jour de version : 3.5.3, 3.5.4, 3.5.6 et 3.5.7 ont été publiées.
- Amélioration de la gestion des messages d'erreur liés aux fichiers. [#1929](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1929)
- Remplacement de la modale asdir par un toast d'erreur. [#1927](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1927)
- Correction de l'affichage de l'analyse doc-ia sur la mise à jour du fichier de salaire. [#1935](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1935)
