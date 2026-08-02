## Changelog : aplypro (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette mise à jour apporte des corrections et améliorations concernant la génération et la gestion des demandes d'autorisation (DA), notamment pour les stages individuels et les paiements. Des ajustements ont également été effectués pour améliorer la gestion des données issues de FREGATA et éviter des erreurs de traitement.

### Évolutions fonctionnelles
- Correction du bouton de génération des demandes d'autorisation (DA) individuelles. [#2000](https://github.com/betagouv/aplypro/issues/2000)
- Demande de confirmation du directeur lors de la génération d'une DA individuelle.
- Correction de la gestion des numéros ADM pour les paiements rejetés, avec génération proactive de nouveaux numéros. [#2002](https://github.com/betagouv/aplypro/issues/2002)
- Blocage des paiements sortants pour les dossiers MASA afin d'éviter des problèmes.
- Prévention de l'envoi d'adresses pour les non-recouvrements. [#1999](https://github.com/betagouv/aplypro/issues/1999)
- Correction de l'injection d'UAI. [#1997](https://github.com/betagouv/aplypro/issues/1997)

### Évolutions techniques
- Refactorisation de l'organisation des vues liées aux décisions d'attribution, regroupées dans un sous-dossier.
- Gestion des conflits dans le mapper FREGATA entre les codes 'division' et 'statutApprenant'. [#1998](https://github.com/betagouv/aplypro/issues/1998)
- Ajout d'une méthode d'instance pour inspecter les données XML envoyées pour une demande de paiement spécifique.
- Ajout de tests unitaires pour améliorer la couverture et la robustesse du code.
- Ajout des attributs manquants dans le mapper des scolarités FREGATA.

### Autres changements
- Suppression des anciennes entités "indus" remplacées par des corrections.
- Mise à jour de la version de l'application.
- Corrections de style avec Rubocop.
