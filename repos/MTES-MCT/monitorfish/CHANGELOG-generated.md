## Changelog : monitorfish (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface de contrôle des navires, notamment pour la gestion des contrôles en mer et à la débarque dans le cadre du projet e-ISR. Des corrections et des optimisations ont été apportées pour améliorer la stabilité et la performance de l'application, ainsi que des mises à jour techniques pour maintenir la sécurité et la compatibilité des dépendances.

### Évolutions fonctionnelles
- Ajout de l'affichage des groupes prioritaires et des signalements de la marée sous la recherche navire dans le cadre des contrôles.
- Possibilité de sauvegarder un contrôle rendu valide après un changement de date de mission.
- Amélioration de l'affichage des informations sur les navires sous AIS v1.2.
- Ajout de la description des groupes prioritaires dans les nouvelles fonctionnalités.
- Ajout d'un engin pour les navires auxiliaires à la campagne BFT.
- Correction de l'affichage du champ infraction dans le formulaire de contrôle.
- Correction de l'affichage des zones attribuées à un contrôle sur la base du JPE.
- Affichage des messages manuels de préavis dans la marée du navire.
- Ajout de la possibilité de ne pas renseigner la zone FAO lors de l'ajout d'une espèce pour les navires de plus de 12m.
- Correction de l'affichage des champs facultatifs dans e-ISR.
- Correction de l'affichage des champs liés aux prises sous-dimensionnées dans e-ISR.
- Ajout des champs armateur au formulaire de contrôle.
- Correction de l'affichage des contrôles en mer et à la débarque pour e-ISR v1.3.
- Correction de l'affichage des contrôles en mer et à la débarque pour e-ISR v1.2.

### Évolutions techniques
- Migration du linter frontend vers OxLint (hybride avec ESLint) pour une meilleure qualité du code.
- Mise à jour des dépendances frontend (uuid, TS-ESLint, styled-components, monitor-ui).
- Amélioration des tests Cypress pour une meilleure couverture et stabilité.
- Optimisation des performances backend avec l'utilisation de ktlint pour le formatage du code.
- Mise en place de git hooks pour garantir la qualité du code.
- Mise à jour des dépendances Python (bleach, cryptography, tornado).
- Ajout d'index pour l'import des notes de vente dans le data warehouse.
- Correction de la sérialisation PATCH.
- Amélioration de la gestion des schémas Zod pour une validation plus robuste.
- Ajout de la gestion du propriétaire du navire (proprietor) via l'API publique et l'intégration avec navpro.

### Autres changements
- Correction de plusieurs problèmes de linting.
- Amélioration de la documentation.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Correction du parser de notes de vente FLUX.
- Correction de la devise des notes de vente.
- Suppression de flag_state des positions AIS.
- Correction de la direction des flèches et des pistes antimeridiennes.
- Correction de l'affichage des étiquettes des cases à cocher JDP dans les tests Cypress.
- Correction de l'affichage des libellés de poids pour les espèces non débarquées.
- Ajout d'une icône d'information.
- Mise à jour de la REG UE pour les avaries VMS et les dysfonctionnements des balises.
- Ajout d'opérateur à l'API publique.
- Correction de l'affichage des tags de groupe de navire et de signalement dans le formulaire de contrôle.
- Correction de l'affichage des groupes dans les tests Cypress.
- Correction de l'affichage des groupes partagés et des signalements de la marée.
- Correction des tests Cypress pour les espèces.
- Correction des tests Cypress pour les contrôles en mer et à la terre.
- Correction de l'activation des lignes d'espèces.
- Correction de l'affichage des champs d'espèces dans les contrôles à la terre et en mer.
- Correction des assertions du sélecteur d'engins de pêche.
- Correction de l'affichage des espèces non débarquées.
- Correction de l'affichage des champs d'espèces et des tableaux de discards après les CI.
- Ajout d'un bouton pour ne pas renseigner les espèces débarquées.
- Conversion des champs d'espèces et de discards en SimpleTable avec édition au survol.
- Correction de l'affichage des champs désactivés dans les contrôles à la terre.
- Correction des assertions du sélecteur d'engins de pêche.
- Correction des schémas Zod.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
- Correction de l'affichage des champs facultatifs.
- Correction de l'affichage des champs obligatoires.
