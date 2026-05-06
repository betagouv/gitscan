## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'analyse des bulletins de salaire (payslips) et l'expérience utilisateur associée, notamment avec l'intégration d'une analyse documentaire intelligente (doc-ia). Des corrections ont également été apportées pour améliorer la validation des dossiers et la gestion des garants. Enfin, des améliorations de l'interface utilisateur et des corrections de bugs ont été implémentées.

### Évolutions fonctionnelles
- Ajout du nom préféré du garant dans le dossier. [#1953](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1953)
- Intégration d'un support de lien vers la documentation de l'analyse IA sur les documents. [#1950](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1950)
- Ajout d'un badge d'erreur au composant de récapitulatif financier (tenantv3). [#1947](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1947)
- Ajout de l'analyse documentaire intelligente (doc-ia) pour les bulletins de salaire. [#1928](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1928)
- Amélioration de l'affichage des messages d'erreur lors de l'analyse des bulletins de salaire. [#1940](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1940)
- Masquage du bouton de réponse dans les messages lorsque le dossier est validé. [#1943](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1943)
- Correction d'un bug empêchant la validation d'un dossier avec un garant personne morale. [#1952](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1952)
- Correction d'un bug empêchant la validation d'un dossier avec un garant personne morale (hotfix). [#1952](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1952)
- Correction de l'affichage des documents lors de la mise à jour d'un fichier de salaire. [#1935](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1935)
- Correction du focus sur le champ somme lors de son état vide (formulaire de salaire). [#1941](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1941)
- Correction de l'affichage des documents lors de l'analyse de la continuité de la fiche de paie. [#1949](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1949)
- Ajout d'un message d'erreur plus clair lors du téléchargement de fichiers non supportés. [#1929](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1929)
- Réinitialisation du formulaire de contact après soumission sur la page d'accueil. [#1945](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1945)

### Évolutions techniques
- Mise à jour des dépendances pour corriger des vulnérabilités (CVE). [#1954](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1954)
- Ajout de la compatibilité avec la règle de feuille d'impôt. [#1946](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1946)
- Refactorisation de la logique de sauvegarde des fichiers pour les salaires avec analyse. [#1939](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1939)
- Amélioration de la gestion de la somme mensuelle dans le formulaire de salaire après suppression de fichier. [#1936](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1936)
- Ajout de tests E2E pour le cas d'utilisation heureux de l'analyse des bulletins de salaire. [#1937](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1937)

### Autres changements
- Publication des versions 3.5.6 et 3.5.7.
- Corrections de QA sur l'analyse des bulletins de salaire. [#1942](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1942)
- Correction de tests QA sur les bulletins de salaire. [#1944](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1944)
