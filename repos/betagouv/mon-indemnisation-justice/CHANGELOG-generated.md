## Changelog : mon-indemnisation-justice (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, l'application Mon Indemnisation Justice a bénéficié d'améliorations significatives en termes de sécurité, de gestion des dossiers et d'expérience utilisateur. Des correctifs ont été apportés pour améliorer la stabilité et la fiabilité de l'application, notamment en corrigeant des erreurs liées à la gestion des adresses, des attestations et des emails. L'accès et la gestion des agents ont également été sécurisés et améliorés.

### Évolutions fonctionnelles
- Correction d'un problème d'affichage du badge "Déclaration FDO" [#cd805a5](https://github.com/betagouv/mon-indemnisation-justice/commit/cd805a5).
- Ajout du type "Avis d'intervention" à la liste des types d'attestation.
- Amélioration de l'affichage de l'explication de la clôture sur la page "Mes demandes".
- Correction d'un lien mort sur la page récapitulative.
- Correction d'un lien mort sur la liste des arrêtés à signer.
- Correction d'un problème lié à l'affichage des montants littéraux (troncature de "zéro centimes").
- Affichage de la première ligne de l'adresse sur l'arrêté de paiement.
- Mise en place d'un cache buster pour éviter les problèmes de chargement des ressources.
- Affichage d'un message de chargement au démarrage de l'application.
- La déclaration n'apparait que si elle est acceptée par le requérant [#8e7351c](https://github.com/betagouv/mon-indemnisation-justice/commit/8e7351c).
- Correction d'un problème lié à la gestion des agents PP et à l'association des agents à leur administration [#9884fc6](https://github.com/betagouv/mon-indemnisation-justice/commit/9884fc6).
- Correction d'un problème lié à la conversion de la casse lors de la connexion et de l'enregistrement des adresses [#550bd32](https://github.com/betagouv/mon-indemnisation-justice/commit/550bd32).
- Ajout d'un motif de clôture "Dossier incomplet".

### Évolutions techniques
- Implémentation de Content Security Policy (CSP) pour renforcer la sécurité de l'application.
- Intégration de Sentry pour la gestion des erreurs et le suivi des performances, incluant la transmission du contexte utilisateur [#9a526f7](https://github.com/betagouv/mon-indemnisation-justice/commit/9a526f7).
- Mise à jour des versions de Symfony et Doctrine pour préparer la migration vers la version 8.0.
- Refonte de la page "Mon compte" en React.
- Conversion du layout de l'espace FIP6.
- Déplacement de la route de recherche de dossiers.
- Séparation des dossiers à instruire de ceux déjà en instruction sur les tableaux de bord.
- Restauration de la réactivité de Mobx.
- Correction de bugs et amélioration des tests unitaires backend.
- Correction de problèmes liés à Doctrine.
- Mise à jour de l'image Docker pour retirer la variable d'environnement APP_RUNTIME.

### Autres changements
- Mise à jour du guide de déclaration PN.
- Correction de typos et amélioration de la qualité du code.
- Correction de l'envoi du courriel de notification de déclaration retournée.
- Ajout de tests unitaires pour l'API.
- Correction de l'affichage du prénom dans certains cas.
- Suppression de la mention "en qualité de" du corps du courrier de décision.
- Clonage de la page "Consulter dossier".
- Correction d'un lien mort depuis les listes de dossiers.
- Correction d'un bug lié à l'affichage du nombre d'arrêtés à signer.
- Correction d'un problème lié à l'opération "insecure".
- Ajout d'emails pour la décision (ok et ko), la confirmation de dépôt et la clôture sans traitement.
- Correction d'un problème lié à l'affichage du badge "Declaration FDO".
- Correction d'un bug lié à l'affichage du badge "Declaration FDO".
- Correction d'un bug lié à l'affichage du badge "Declaration FDO".
