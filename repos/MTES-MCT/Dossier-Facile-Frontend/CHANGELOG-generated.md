## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des garants et l'analyse des justificatifs de domicile. Des corrections de bugs et des améliorations de la sécurité ont également été apportées. Plusieurs versions ont été publiées (3.5.6, 3.5.7, 3.5.8 et 3.5.9) intégrant ces changements.

### Évolutions fonctionnelles
- Ajout d'un bouton de suppression de garant sur la page de validation du dossier [#1966](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1966).
- Possibilité de renseigner le nom préféré du garant [#1953](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1953).
- Ajout d'un lien d'aide et de support concernant les documents analysés (bulletins de salaire) [#1950](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1950).
- Amélioration de l'affichage des documents lors de l'analyse des bulletins de salaire [#1949](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1949).
- Ajout d'un badge d'erreur au composant de récapitulatif financier [#1947](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1947).
- Correction d'un bug empêchant la validation d'un dossier avec un garant légal [#1885a978](https://github.com/MTES-MCT/Dossier-Facile-Frontend/commit/1885a978).
- Correction d'un bug empêchant la soumission d'une demande avec un garant vide [#1952](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1952).
- Mise à jour du libellé de l'année de l'avis d'imposition pour la location et la pension [#1968](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1968).
- Correction de la marge supérieure du bouton de suppression du garant [#1967](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1967).
- Ajout d'une enquête lors du téléchargement d'une archive non vérifiée [#1957](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1957).
- Ajout d'un événement Matomo pour suivre l'utilisation du lien d'aide sur l'analyse des documents [#1956](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1956).
- Correction de régressions des tests E2E [#1959](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1959).
- Correction du type de contenu des en-têtes [#1958](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1958).

### Évolutions techniques
- Mise à jour des dépendances pour corriger des vulnérabilités (CVE) [#1954](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1954).
- Remplacement du modal DSFR par un modal Typeform pour l'enquête [#1961](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1961).
- Amélioration de la compatibilité avec les règles de feuille de taxe [#1946](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1946).
- Suppression de l'enquête pour les codes postaux non vérifiés [#1963](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1963).
- Désactivation de l'autocomplétion incorrecte pour le nom préféré du garant [#1955](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1955).

### Autres changements
- Publication des versions 3.5.6, 3.5.7, 3.5.8 et 3.5.9.
- Correction de bugs et améliorations diverses de la qualité du code.
- Reset du formulaire de contact après soumission [#1945](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1945).
