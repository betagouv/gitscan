## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment au niveau de la gestion des garants et de l'analyse des justificatifs de domicile. Des corrections de bugs ont également été apportées pour améliorer la stabilité de l'application et résoudre des problèmes spécifiques rencontrés par les utilisateurs, en particulier concernant la validation des dossiers et l'affichage des informations.

### Évolutions fonctionnelles
- Ajout du nom préféré du garant lors de la saisie des informations. [#1953](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1953)
- Amélioration de la gestion des justificatifs de domicile : masquage des documents actuels lorsqu'ils sont vides lors de l'analyse des bulletins de paie. [#1949](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1949)
- Ajout d'un lien d'aide contextuelle concernant les documents à fournir lors de l'analyse des bulletins de paie. [#1956](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1956)
- Ajout d'un badge d'erreur au composant de récapitulatif financier (tenantv3). [#1947](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1947)
- Correction d'un bug empêchant la validation d'un dossier avec un garant personne morale. [#1885a978](https://github.com/MTES-MCT/Dossier-Facile-Frontend/commit/1885a978)
- Correction d'un bug empêchant la soumission d'une demande avec un garant vide. [#1952](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1952)
- Ajout d'une enquête (survey) lors du téléchargement d'archives non vérifiées. [#1957](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1957)
- Suppression de l'enquête pour les archives non vérifiées. [#1963](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1963)
- Désactivation de l'autocomplétion incorrecte pour le nom préféré du garant. [#1955](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1955)
- Réinitialisation du formulaire de contact après soumission. [#1945](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1945)
- Masquage du bouton de réponse dans les messages lorsque le locataire est validé. [#1943](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1943)

### Évolutions techniques
- Mise à jour des dépendances pour corriger des vulnérabilités (CVE). [#1954](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1954)
- Ajout de la compatibilité avec la règle de feuille d'impôt (tax leaf rule) pour l'analyse des justificatifs. [#1946](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1946)
- Correction du type de contenu (contentType) récupéré depuis les headers. [#1958](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1958)
- Correction de régressions des tests E2E. [#1959](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1959)
- Remplacement du modal DSFR par un modal Typeform pour l'enquête. [#1961](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1961)
- Nouvelle tentative d'intégration du modal Typeform. [#1960](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1960)

### Autres changements
- Corrections et améliorations diverses pour la qualité du code et la maintenance du projet.
- Publication des versions 3.5.6, 3.5.7, 3.5.8 et 3.5.9.
